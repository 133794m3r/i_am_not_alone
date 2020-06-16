from .hotline_db import hotline_db

class crisis_numbers(hotline_db.Document):
    country = hotline_db.StringField(required=True, unique=True)
    numbers = hotline_db.StringField(required=True)
    website = hotline_db.StringField(required=True)