
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, redirect
import os

#@route('/')
#def graph():
#    with open("/home/dzil123/graph/graph.html", "r") as o:
#        return o.read()

@route('/')
def index():
    redirect("/index.html")

@route('/static')
def ls():
    return str(os.popen('ls -lARh /home/dzil123/graph').read().replace('\n', '<br/>'))

application = default_app()

