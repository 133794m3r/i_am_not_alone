from .db import db

class GEOIP(db.Document):
    network = db.IntField(required=True, unique=True)
    geoname_id = db.IntField(required=True)
    continent_code = db.StringField(required=True)
    continent_name = db.StringField(required=True)
    country_iso_code = db.StringField(required=True)
    country_name = db.StringField(required=True)
    is_anonymous_proxy = db.IntField(required=True)
    is_satellite_provider = db.IntField(required=True)