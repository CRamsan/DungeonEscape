#!/usr/local/bin/python2

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
             
        arguments = filter(None, self.path.split('/'))
           
        result = self.post_Execute(arguments, form)
        self.wfile.write(result)
        return

    def get_Execute(self, path, query):
        if len(path) == 0:
            return server.game.to_json()
        elif len(path) == 1:
            return server.game.get_player(path[0]).to_json()
        elif len(path) == 2:
            player = server.game.get_player(path[0])
            if player.validate_token(path[1]) :
                return server.game.get_player(path[0]).units_to_json()
            else:
                return '{"result":"failed", "reason":"error while authorizing"}'
        elif len(path) == 3:
            player = server.game.get_player(path[0])
            target = None
            if player.validate_token(path[2]) :
                target = player.get_unit(path[1])
            else:
                return '{"result":"failed", "reason":"error while authorizing"}'
            val = query.split('=')[1]
            if val == 'unit_info':
                return target.to_json()
            elif val == 'unit_vision':
                return server.game.vision_to_json(target)
        return '{"result":"failed", "reason":"error while parsing arguments"}'
    
    def post_Execute(self, path, form):
        if len(path) == 0:
            return
        elif len(path) == 1:
            if path[0] == 'join':
                return server.join_game(form[form.keys()[0]].value) 
            else :
                return '{"result":"failed"}, "reason":"error while parsing argument"'
        else :
            player = server.game.get_player(path[0])
            if player.validate_token(path[2]) :
                unit = player.get_unit(path[1])
                return server.game.execute_command(player.id, unit.id , form[form.keys()[0]].value) 
            else:   
                return '{"result":"failed"}, "reason":"error while authorizing"'


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
        if len(self.game.players) < 4:
            print name + ' is waiting'
            self.semafore.wait()
            print name + ' can continue'
            self.semafore.release()
            
            return '{ "playerID" : "' + newPlayer[0] + '", "playerToken" : "' + newPlayer[1] + '"}'
        elif len(self.game.players) == 4:                        
            print name + ' is last player, sending signal'
            self.semafore.notify_all()
            self.game.generate_the_map()
            return '{ "playerID" : "' + newPlayer[0] + '", "playerToken" : "' + newPlayer[1] + '"}'
        else:
            print name + ' is trying to join but game is full'
            return '{"result":"failed", "reason":"game is full"}'



    
    def start_game(self, name):
        print 'All players ready, starting game'
            
if __name__ == "__main__":
    server = ThreadedHTTPServer(('localhost', 8888), GetHandler)
    print 'Starting server'
    server.init_game()
    viz = Visualizer()
    
    try:
        vis_thread = threading.Thread(target=viz.vis_loop, args=(server.game,))
        vis_thread.start()
    except:
        print "Error: unable to start vis thread"
        
    server.serve_forever()
    sys.exit(0)
