# #!flask/bin/python
# from flask import Flask, jsonify,request

# app = Flask(__name__)
# @app.route('/',methods=['GET','POST']) #this route on top of a function turns it into a uri endpoint
# def index():
#     if(request.method=='POST'):
#         some_json=request.get_json()
#         return jsonify({'you sent': some_json}),201
#     else:
#         return jsonify({'about': "hello "})

# @app.route('/multi/<int:num>', methods=['GET'])
# def get_multiply10(num):
#     return jsonify({'result':num*10})
# if __name__ == '__main__':
#     app.run(debug=True)

#!/usr/bin/env python
import requests
from datetime import date, datetime
#from season import get_season
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
import os
import sys
from io import BytesIO
import re
import difflib
from flask import Flask,request, url_for
from googleOCR import find_brand_from_image 
from setUpDB import my_database
from flask_restful import Resource, Api #resource allows code to be much more segregated 
import time

app = Flask(__name__)
api=Api(app)

my_DB=my_database()

class HelloWorld(Resource):
    def get(self):  
        print('GET')      
        return {'about': "hello "}

    def post(self):
        print('POST')
        # my_data=request.get_data()
        
        # newFile = open("new_image.jpg", "wb") #open data as binary
        # newFile.write(my_data) #write data
        # time.sleep(1)
        brand=find_brand_from_image()
        
        return {'my brand': brand}
        # file = request.files['file']
        # fname = secure_filename(file.filename)
        # file.save('static/' + fname)
        # # do the processing here and save the new file in static/

        # fname_after_processing = fname
        # return {'produce': request.get_json()[], 'numBugs': 3,'result_image_location': url_for('static', filename=fname_after_processing)}, 201 #change the default code

class Multi(Resource):
    def get(self,num):
        return{'result':num*10}

api.add_resource(HelloWorld,'/')
api.add_resource(Multi,'/multi/<int:num>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)