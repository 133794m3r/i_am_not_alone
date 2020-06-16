from .db import db

class Ip_address_map(db.Document):
    start_int = db.IntField(required=True, unique=True)
    end_int = db.IntField(required=True)
    geoname_id = db.IntField(required=True)
    continent_name = db.StringField(required=True)
    country_iso_code = db.StringField(required=True)
    country_name = db.StringField(required=True)
    continent_name = db.StringField(required=True)
    start=db.StringField(required=True)
    end=db.StringField(required=True)
