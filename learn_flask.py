from flask import Flask,redirect,url_for,render_template
import requests
import time

webapp = Flask(__name__)

BASE = "http://127.0.0.1:5000/" 
#@webapp.route('/Sam')
#def home(name):
#    return render_template("index.html",content=['Sam','Vedant','Aryan'])
#response = requests.put(BASE + "Functions" , {"command":"synonym of nice"})

#name = response.json

      
@webapp.route('/Sam')
def user():
    response = requests.get(BASE + "Functions")
    time.sleep(5)
    name = response.json()
    return render_template("index.html",WebpageTitle=name)

#@webapp.route('/admin')
#def admin():
#    return redirect(url_for("user",name="Admin!"))


if __name__ == "__main__":
    webapp.run()
