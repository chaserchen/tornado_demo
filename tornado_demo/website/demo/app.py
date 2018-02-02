# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado_demo.website.demo.index import IndexHandler

tornado.options.define('port', default=8000, help='run on the given port', type=int)
tornado.options.parse_command_line()
app = tornado.web.Application(handlers=[
    (r'/', IndexHandler),
])
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(tornado.options.options.port)
tornado.ioloop.IOLoop.instance().start()
