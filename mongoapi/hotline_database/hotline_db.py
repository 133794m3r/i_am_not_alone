from flask_mongoengine import MongoEngine

hotline_db = MongoEngine()

def hotline_initialize_db(app):
    hotline_db.init_app(app)