from flask import Flask,session,render_template,redirect,abort,url_for,request, Response,jsonify
from flask_mongoengine import MongoEngine
from flask_session import Session
from flask_pymongo import PyMongo

import eliza
def init_session(name):
    session['handle'] =name
    session['eliza'] = eliza.Eliza()
    session['eliza'].load('doctor.txt')
    return session['eliza'].initial()

app = Flask(__name__)
app.config.from_pyfile('config.py')
Session(app)

db = MongoEngine()
mongo = PyMongo(app)

with app.app_context():
   db.init_app(app)
   try:
       db_client = db.connection['flask_webapp_db']
   except ConnectionFailure as e:
       sys.stderr.write("Could not connect to MongoDB: %s" % e)
       sys.exit(1)

@app.route('/crisis/<specific_ip>')
def get_ips(specific_ip):
    from ipaddress import IPv4Address
    specific_ip=int(IPv4Address(specific_ip))
    ips=mongo.db.ip_address_map.find_one({"start_int":{"$lte":specific_ip},"end_int":{"$gte":specific_ip}}
                                             ,{"_id":0,"end":0,"geoname_id":0,"start":0,"end":0,"country_iso_code":0})
    if ips is None:
        return jsonify({'err':"private ip address found"})
    country=ips['country_name']
    response=mongo.db.crisis_numbers.find_one({"country":country},{"_id":0})
    if response is None:
        response="Please look for a local crisis hotline number on your search engine."
    return jsonify(response)

@app.route('/')
def index():
    import os
    return os.getenv('mdb_pass')
@app.route('/chat',methods=["POST","GET"])
def chat():
    if request.method == "GET":
        if len(request.args) > 0:
            if session.get('handle') is None:
                name=request.args.get('name')
                return init_session(name)
            else:
                if request.args.get('msg') is not None:
                    return session['eliza'].respond(request.args.get('msg'))
                else:
                    return "No msg received"
        else:
            return "nothing received"
    else:
        if session.get('handle') is None:
            name=request.form.get('name')
            return init_session(name)
        else:
            if request.form.get('msg') is not None:
                return session['eliza'].respond(request.form.get('msg'))
            else:
                return "No msg received"


if __name__ == '__main__':
    app.SECRET_KEY = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.secret_key = 'super secret key'
    app.run(debug=true,SECRET_KEY="secret")
