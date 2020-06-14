from flask import Flask, request, Response
from database.db import initialize_db
from database.model import GEOIP
from hotline_database.hotline_db import hotline_initialize_db
from hotline_database.hotline_model import Hotline

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/all-geoips'
}

@app.route('/ips') 
def get_ips():
    ips = GEOIP.objects.to_json()
    return Response(ips, mimetype="application/json", status=200)

@app.route('/ips/<specific_ip>')
def get_specific_ips(specific_ip):
    c_name = GEOIP.objects.get(specific_ip__gte=GEOIP.network).first.to_json()
    hotline = Hotline.objects.get(c_name=Hotline.country_name).to_json()
    return Response(hotline, mimetype="application/json", status=200)

initialize_db(app)

app.run()