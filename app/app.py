from flask import Flask,session,render_template,redirect,abort,url_for,request
from flask_session import Session
import eliza
def init_session(name):
	session['handle'] =name
	session['eliza'] = eliza.Eliza()
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
