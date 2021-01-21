from flask import Flask,redirect,url_for,render_template
import requests

webapp = Flask(__name__)

BASE = " http://127.0.0.1:5000/" 
#@webapp.route('/Sam')
#def home(name):
#    return render_template("index.html",content=['Sam','Vedant','Aryan'])
        
@webapp.route('/<name>')
def user(name):
    response = requests.get(BASE + "Functions")
    name = response.json()
    return render_template("index.html",WebpageTitle=name)

#@webapp.route('/admin')
#def admin():
#    return redirect(url_for("user",name="Admin!"))


if __name__ == "__main__":
    webapp.run(host='0.0.0.0',port=12345)
