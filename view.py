import webapp2
import template_wrangler
from google.appengine.ext import ndb
import db_defs
import string
from time import sleep

class View(template_wrangler.TemplateHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_variables ={}

    def render(self, page):
        # Query datastore for existing characters
        self.template_variables['products'] = [{
            'key'   : x.key.urlsafe(),
            'clicks': x.clicks,
            'date'  : x.date,
            'name'  : x.name
            } for x in db_defs.Product.query().order(db_defs.Product.date).fetch()]
        template_wrangler.TemplateHandler.render(self, page, self.template_variables)

    def post(self):
        if self.template_variables['form_content']['action'] == "click":
            #click
            prod_key = ndb.Key(urlsafe=self.request.get('key'))
            product = prod_key.get()
            product.clicks = product.clicks + 1
            product.put()
            sleep(1)
            self.render('view.html')
