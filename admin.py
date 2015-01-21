import webapp2
import template_wrangler
from google.appengine.ext import ndb
import db_defs
import string
from time import sleep


class Admin(template_wrangler.TemplateHandler):
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
        # Initialize template variables
        self.template_variables['form_content'] = {}
        self.template_variables['message'] = []
        self.template_variables['errors'] = False
        exists = False

        # Get form data
        for i in self.request.arguments():
            self.template_variables['form_content'][i] = self.request.get(i)

        # Check desired action, take appropriate steps
        if self.template_variables['form_content']['action'] == "delete":
            #delete entry
            prod_key = ndb.Key(urlsafe=self.request.get('key'))
            product = prod_key.get()
            product.key.delete()
            sleep(1)
            self.render('admin.html')
        
        else:
            # Form validation
            if not self.template_variables['form_content']['name'] or string.strip(self.template_variables['form_content']['name'], " ") == "":
                self.template_variables['message'].append("ERROR: Name cannot be blank.")
                self.template_variables['errors'] = True

            # Add data to datastore
            if self.template_variables['errors']:
                self.render('admin.html')
            elif self.template_variables['form_content'].has_key('key'):
                key = ndb.Key(urlsafe=self.template_variables['form_content']['key'])
                product = key.get()
                exists = True
            else:
                key = ndb.Key(db_defs.Product, 'products')
                product = db_defs.Product(parent=key)
            
            product.name = string.strip(self.template_variables['form_content']['name'], " ")
            product.clicks = 0
            product.put()
            self.template_variables['message'] = ['"'+product.name + '" was added to the database.']
            sleep(1)
            self.render('admin.html')

    def get(self):
        self.render('admin.html')
