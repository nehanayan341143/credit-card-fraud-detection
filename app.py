# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 21:35:23 2021

@author: Neha
"""

import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# prediction function 
def ValuePredictor(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 7) 
    loaded_model = pickle.load(open("model.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0]    

  

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
    if int(result)== 1:
        prediction ='Given transaction is fradulent'
        mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
        try:
            mail_server.login("0126cs191064@oriental.ac.in", "abcd@123456")
        except:
            pass

        message = EmailMessage()

        message['To'] = "kneha4876@gmail.com"
        message['From'] = "0126cs191064@oriental.ac.in"
        message['Subject'] = 'Alert!!!'
        body="""Fraud Transaction detected
                Please contact your bank
                   
                
                Do not reply to this mail"""
        message.set_content(body)
        
        try:
            mail_server.send_message(message)
        except:
            pass
        finally:
            mail_server.quit()
    else:
        prediction ='Given transaction is NOT fradulent'            
    return render_template("result.html", prediction = prediction) 
    
    
    
    
    
                  
if __name__ == "__main__":
    app.run(debug=True)