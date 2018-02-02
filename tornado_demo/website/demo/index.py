# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division

import tornado.httpclient
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'hello')
        self.write(greeting + ', friendly user!')
