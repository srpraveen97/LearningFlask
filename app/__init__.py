from flask import Flask

import flask

print(flask.__version__)

app = Flask(__name__)

from app import views
from app import admin_views

