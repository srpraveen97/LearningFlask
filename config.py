class Config():
    DEBUG = False
    TESTING = False
    
    SECRET_KEY = "dksjfkdj;fgagj;dgj"
    
    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    
    # /mnt/c/Praveen/Projects/FlaskLearning/
    
    IMAGE_UPLOADS = "app/static/img/uploads"
    ALLOWED_IMAGE_EXTENTIONS = ["PNG","JPG","JPEG","GIF"]
    MAX_CONTENT_LENGTH = 50*1024*1024
    
    SESSION_COOKIE_SECURE = True
    
class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    
    DEBUG = True
    
    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    SESSION_COOKIE_SECURE = False
    
class TestingConfig(Config):
    TESTING = True
    
    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    
    UPLOADS = "/home/username/projects/flask_test/app/static/images/uploads"
    
    SESSION_COOKIE_SECURE = False
    
    
    
