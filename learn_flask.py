from flask import Flask,redirect,url_for,render_template
import requests
import time
from flask_restful import Api, Resource, reqparse


webapp = Flask(__name__)
api = Api(webapp)


reqobj = reqparse.RequestParser()
reqobj.add_argument("searchbox", type=str, help="Command is required")

BASE = "http://127.0.0.1:5000/"

@webapp.route('/<query>')
def Home(query):
    print(query)
    response = requests.put(BASE + "Functions" ,{"command":query})
    name = response.json()
    return render_template("index.html",WebTitle=name)
        
           
class Html_query(Resource):
    def get(self):
        args = reqobj.parse_args()
        query = args['searchbox']
        print(query)
        return redirect(url_for("Home", query = query))


api.add_resource(Html_query, "/HTML")

if __name__ == "__main__":
    webapp.run()
