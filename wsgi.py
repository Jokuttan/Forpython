#!/usr/bin/env python

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["<h1 style='color:blue'>Hello joelta!</h1>"]
print('Hello, joel!')
