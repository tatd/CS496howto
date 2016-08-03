import webapp2
from views import *

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/create', CreateHandler),
    ('/edit', EditHandler),
    ('/page1', Page1Handler),
    ('/page2', Page2Handler),
    ('/page3', Page3Handler),
    ('/page4', Page4Handler),
    ('/page5', Page5Handler)
], debug=True)
