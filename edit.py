import webapp2
import template_wrangler
from google.appengine.ext import ndb
import db_defs

class Edit(template_wrangler.TemplateHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_variables ={} 

    def get(self):
        char_key = ndb.Key(urlsafe=self.request.get('key'))
        character = char_key.get()
        print "DEBUG"
        print character
        print "DEBUG"
        self.template_variables['character'] = character
        self.render('edit.html', self.template_variables)

