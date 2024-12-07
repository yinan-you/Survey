from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/') # whenever we go to / route, we will run this. This is the homepage
def home():
    return "<h1>Test</h1>"