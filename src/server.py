#!/usr/local/bin/python2.7
# encoding: utf-8

import sys
import os

from BaseHTTPServer import BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn
import threading
import urlparse
import cgi

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.send_response(200)
        self.end_headers()
        message =  threading.currentThread().getName()
        self.wfile.write(message)
        self.wfile.write('\n')
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
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Client: %s\n' % str(self.client_address))
        self.wfile.write('Path: %s\n' % self.path)
        self.wfile.write('Form data:\n')
        
        # Echo back information about what was posted in the form
        for field in form.keys():
            field_item = form[field]
        if field_item.filename:
            # The field contains an uploaded file
            file_data = field_item.file.read()
            file_len = len(file_data)
            del file_data
            self.wfile.write('\tUploaded %s (%d bytes)\n' % (field, 
            file_len))
        else:
            # Regular form value
            self.wfile.write('\t%s=%s\n' % (field, form[field].value))
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == "__main__":
    server = ThreadedHTTPServer(('localhost', 8686), GetHandler)
    print 'Starting server'
    server.serve_forever()    
    sys.exit(0)
