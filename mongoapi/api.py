from flask import Flask, request, Response
from database.db import initialize_db
from database.model import Ip_address_map
from hotline_database.hotline_db import hotline_initialize_db
from hotline_database.hotline_model import Crisis_numbers
import os
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': "mongodb+srv://{0}:{1}@mlh-summer-hacks-dqi2z.gcp.mongodb.net/geo_ip_data?retryWrites=true&w=majority".format(os.getenv('mdb_user'),os.getenv('mdb_pass'))

}

@app.route('/ips')
def get_ips():
    ips = Ip_address_map.objects.to_json()
    return Response(ips, mimetype="application/json", status=200)

@app.route('/ips/<specific_ip>')
def get_specific_ips(specific_ip):
    c_name = Ip_address_map.objects.get(specific_ip__gte=GEOIP.network).first.to_json()
    hotline = Hotline.objects.get(c_name=Hotline.country_name).to_json()
    return Response(hotline, mimetype="application/json", status=200)

initialize_db(app)

app.run()
