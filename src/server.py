#!/usr/local/bin/python2.7
# encoding: utf-8

import sys

from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn

import threading
import urlparse
import cgi

import game
from game import Game
from miro.databaseupgrade import get_next_id

server = None;

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
        pass
    
    def post_Execute(self, path, form):
        if len(path) == 0:
            return
        elif len(path) == 1:
            if path[0] == 'join':
                print server.joing_game(form[form.keys()[0]].value)
                return 'joined'
            else :
                return 'failed'
        else :
            player = server.get_game(path[0]).get_player(path[1])
            if player.validate_token(path[2]) :
                player.get_unit(path[3])
            return
        pass


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    games = []
    
    def start_new_game(self):
        print 'Creating new game'
        newGame = Game()
        newGame.start_new_game()
        self.games.append(newGame)
        return newGame.id
    
    def joing_game(self, name):
        print 'Looking for a game where' + name + 'can be added'
        game = self.get_next_game()
        newPlayer = game.add_new_player(name)
        return [game.id, newPlayer[0], newPlayer[1]]
    
    def get_next_game(self):
        for game in self.games:
            if len(game.players) < 4:
                print 'Game found'
                return game
        return self.get_game(self.start_new_game())
    
    def get_game(self, gameid):
        for game in self.games:
            if game.id == gameid:
                return game

if __name__ == "__main__":
    server = ThreadedHTTPServer(('localhost', 8686), GetHandler)
    print 'Starting server'
    server.serve_forever()    
    sys.exit(0)
