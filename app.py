"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask_restful import Resource, Api
import math

app = Flask(__name__)
api = Api(app)


# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

class aoc(Resource):

    def get(self, rad):
        area = math.pi*rad*rad
        return{'Area of Circle':area}
    

class aorec(Resource):
     
    def get(self, length, width):
        area = length * width
        return{'Area of Rectangle':area} 

class aotri(Resource):
     
    def get(self, base, height ):
        area = 1/2*base * height
        return{'Area of Triangle':area} 


       
api.add_resource(aoc, '/aoc/<int:rad>')
api.add_resource(aorec, '/aorec/<int:length>/<int:width>')
api.add_resource(aotri, '/aotri/<int:base>/<int:height>')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
