from flask import Blueprint
#create blueprint to recall the views
main = Blueprint('main', __name__)

from . import views, errors
