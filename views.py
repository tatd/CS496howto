import webapp2
import cgi
import jinja2
import os

from datetime import datetime

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

jinja_environment.globals['year'] = datetime.now().year

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja_environment.get_template('template/index.html')
        self.response.out.write(template.render(template_values))

class Page1Handler(webapp2.RequestHandler):
    def get (self):
        template_values = {}
        template = jinja_environment.get_template('template/page1.html')
        self.response.out.write(template.render(template_values))

class Page2Handler(webapp2.RequestHandler):
    def get (self):
        template_values = {}
        template = jinja_environment.get_template('template/page2.html')
        self.response.out.write(template.render(template_values))


class Page3Handler(webapp2.RequestHandler):
    def get (self):
        template_values = {}
        template = jinja_environment.get_template('template/page3.html')
        self.response.out.write(template.render(template_values))

class Page4Handler(webapp2.RequestHandler):
    def get (self):
        template_values = {}
        template = jinja_environment.get_template('template/page4.html')
        self.response.out.write(template.render(template_values))

class Page5Handler(webapp2.RequestHandler):
    def get (self):
        template_values = {}
        template = jinja_environment.get_template('template/page5.html')
        self.response.out.write(template.render(template_values))

class AppHandler(webapp2.RequestHandler):
    def get (self):
        template_values = {}
        template = jinja_environment.get_template('template/app.html')
        self.response.out.write(template.render(template_values))

class CreateHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja_environment.get_template('template/create.html')
        self.response.out.write(template.render(template_values))

class EditHandler(webapp2.RequestHandler):
    def get (self):
        template_values = {}
        template = jinja_environment.get_template('template/edit.html')
        self.response.out.write(template.render(template_values))

