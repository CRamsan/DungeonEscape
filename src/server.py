#!/usr/local/bin/python2
# encoding: utf-8

import sys
import threading
from viz import Visualizer

from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn

import urlparse
import cgi

from game import Game

server = None;
viz = None

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        message = '|'.join([
        threading.currentThread().getName(),
        'client_address=%s (%s)' % (self.client_address,self.address_string()),
        'command=%s' % self.command,
        'path=%s' % parsed_path.path,
        'query=%s' % parsed_path.query,
        ]) 
        print message
        
        arguments = filter(None, parsed_path.path.split('/'))
        result = self.get_Execute(arguments, parsed_path.query)
        self.wfile.write(result)
        return

    def do_POST(self):
        # Parse the form data posted
        form = cgi.FieldStorage(
        fp=self.rfile, 
        headers=self.headers,
        environ={'REQUEST_METHOD':'POST',
        'CONTENT_TYPE':self.headers['Content-Type'],
        })
        
        # Begin the response
        message = '|'.join([
        threading.currentThread().getName(),
        'client_address=%s (%s)' % (self.client_address,self.address_string()),
        'command=%s' % self.command,
        'path=%s' % self.path])
        
        arguments = filter(None, self.path.split('/'))
        
        for field in form.keys():
            message = '|'.join([message,'%s=%s' % (field, form[field].value)])
        print message
        
        result = self.post_Execute(arguments, form)
        self.wfile.write(result)
        return

    def get_Execute(self, path, query):
        if len(path) == 0:
            return "game data"
        elif len(path) == 1:
            player = server.game.get_player(path[0])
            return "player data"
        elif len(path) == 3:
            player = server.game.get_player(path[0])
            if player.validate_token(path[1]) :
                player.get_unit(path[2])
            else:
                return 'authentication failed'
            val = query.split('=')[0]
            if val == 'unit_info':
                return 'unit found'
            elif val == 'unit_status':
                return 'unit status'
        return 'not valid'
    
    def post_Execute(self, path, form):
        if len(path) == 0:
            return
        elif len(path) == 1:
            if path[0] == 'join':
                print server.join_game(form[form.keys()[0]].value)
                return 'joined'
            else :
                return 'failed'
        else :
            player = server.game.get_player(path[0])
            if player.validate_token(path[1]) :
                player.get_unit(path[2])
            return
        


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    
    game = None
    semafore = None
    
    def init_game(self):
        print 'Starting to listen for players'
        self.game = Game()
        self.game.start_new_game()
        self.semafore = threading.Condition()
    
    def join_game(self, name):
        print 'Adding ' + name + ' to game'
        newPlayer = self.game.add_new_player(name)
        self.semafore.acquire()
        if len(self.game.players) == 4:
            print name + ' is last player, sending signal'
            self.semafore.notify_all()
        else:
            print name + ' is waiting'
            self.semafore.wait()
            print name + ' can continue'
        self.semafore.release()
        return [self.game.id, newPlayer[0], newPlayer[1]]
    
    def start_game(self, name):
        print 'All players ready, starting game'
            
if __name__ == "__main__":
    server = ThreadedHTTPServer(('localhost', 1866), GetHandler)
    print 'Starting server'
    server.init_game()
    viz = Visualizer()
    
    try:
        vis_thread = threading.Thread(target=viz.vis_loop, args=(server.game,))
        vis_thread.start()
    except:
        print "Error: unable to start vis thread"
        
    '''server.serve_forever()'''    
    sys.exit(0)
