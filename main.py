#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import template_wrangler
from google.appengine.ext import ndb
import db_defs
from time import sleep
import datetime
import string

class MainHandler(template_wrangler.TemplateHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_variables ={} 

	def render(self, page):
		# Query datastore for existing characters
		self.template_variables['products'] = [{
			'key'       : x.key.urlsafe(),
			'clicks'	: x.clicks,
			'age'      : (datetime.datetime.utcnow() - x.date).days,
			'name'      : x.name
		} for x in db_defs.Product.query().order(db_defs.Product.date).fetch()]
		template_wrangler.TemplateHandler.render(self, page, self.template_variables)
    
	def get(self):
		self.render('view.html')

        def post(self):
            if self.request.get('action') == "click":
                #click
                prod_key = ndb.Key(urlsafe=self.request.get('key'))
                product = prod_key.get()
                product.clicks = product.clicks + 1
                product.put()
                sleep(1)
                self.render('view.html')   

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/admin', 'admin.Admin'),
], debug=True)
