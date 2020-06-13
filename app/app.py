from flask import Flask,session,render_template,redirect,abort,url_for,request,jsonify
from flask_session import Session
import eliza
#from json import loads as json_parse
def init_session(name):
	session['handle']=name
	session['eliza']=eliza.Eliza()
	session['eliza'].load('doctor.txt')
	return session['eliza'].initial()

app = Flask(__name__)
app.config.from_pyfile('config.py')
Session(app)
@app.route('/')
def index():
	return "done"
@app.route('/chat',methods=["POST","GET"])
def chat():
	user_msg=''
	user_data={}
	response_msg=''
	if request.method == "GET":
		if len(request.args) > 0:
			if session.get('handle') is None:
				name=request.args.get('name')
				response_msg=init_session(name)
			else:
				response_msg=session['eliza'].respond(request.args.get('msg'))
		else:
			return "nothing received"
	else:
		user_data=request.get_json()
		if session.get('handle') is None:
			response_msg=init_session(user_data.get('name'))
		else:
			#if request.form.get('msg') is not None:
			response_msg=session['eliza'].respond(user_data.get('msg'))
		if "COVID19_RESP" in response_msg:
			pass
		elif "SUICIDE_RESP" in response_msg:
			pass
	return jsonify({'name':'eliza','msg':response_msg})
@app.route('/chatter')
def chatter():
	session.clear()
	return app.send_static_file('chatter.html')

if __name__ == '__main__':
	app.SECRET_KEY = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	sess.init_app(app)
	app.secret_key = 'super secret key'
	app.run(debug=true,SECRET_KEY="secret")
