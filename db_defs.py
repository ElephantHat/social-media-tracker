from google.appengine.ext import ndb
import datetime

class Product(ndb.Model):
    name = ndb.StringProperty(required=True)
    clicks = ndb.IntegerProperty(required=True)
    date = ndb.DateTimeProperty(auto_now=True, required=True)
