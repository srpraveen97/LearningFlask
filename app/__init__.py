from flask import Flask
import config

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object(config.ProductionConfig)
    
if app.config["ENV"] == "testing":
    app.config.from_object(config.TestingConfig)
    
else:
    app.config.from_object(config.DevelopmentConfig)

from app import views
from app import admin_views