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
from PIL import Image
import os
import sys
from io import BytesIO
import re
import difflib
from flask import Flask,request, url_for, jsonify
from googleOCR import find_brand_from_image 
from article_classification import *
from setUpDB import my_database
from flask_restful import Resource, Api #resource allows code to be much more segregated 
from flask_cors import CORS, cross_origin

my_DB=my_database()

app = Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS']='Content-Type'

@app.route('/',methods=['GET','POST'])
@cross_origin()


def index():
    if(request.method=='GET'):
        print('GET')  
        #get a string, apply trudie's function, return jso

        return jsonify({'about': "hello worldh"})

    elif(request.method=='POST'):
        my_data=request.get_json(force=True)
        site=my_data["website"]
        gender=my_data["gender"]
        my_type, recommended_colours = article_class(site)
        
        rows,alternatives= my_DB.getRowsFromDB(my_type,recommended_colours,gender)
        return jsonify({'suggestion': rows,'alternatives':alternatives})
    else:
        return "hello world"
        # my_data=request.get_data()
        
        # newFile = open("new_image.jpg", "wb") #open data as binary
        # newFile.write(my_data) #write data
        # time.sleep(1)
        
            # file = request.files['file']
        # fname = secure_filename(file.filename)
        # file.save('static/' + fname)
        # # do the processing here and save the new file in static/

        # fname_after_processing = fname
        # return {'produce': request.get_json()[], 'numBugs': 3,'result_image_location': url_for('static', filename=fname_after_processing)}, 201 #change the default code


#port = int(os.environ.get("PORT", 5000))
if __name__ == '__main__':
    app.run()
