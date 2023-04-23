from flask import Flask
from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app


app = Flask(__name__)

@app.route('/')
def hello_world():    
    return("HELLO WORLD") 

@app.route('/metrics')
def metrics_prometheus():
    return DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})



