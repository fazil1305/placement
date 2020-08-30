from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
app = Flask(__name__)
model = pickle.load(open("placement__.pkl", "rb"))
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict",methods=['POST'])
def predict():
    
    if request.method == 'POST':
        ssc_p=float(request.form['ssc_p'])
        hsc_p=float(request.form['hsc_p'])
        degree_p=float(request.form['degree_p'])
        etest_p=float(request.form['etest_p'])
        gender_M=request.form['gender_M']
        if (gender_M=='M'):
            gender_M=1
        else:
            gender_M=0
        
            
        workex_Yes=request.form['workex_Yes']
        if (workex_Yes=='Yes'):
            workex_Yes=1
        else:
            workex_Yes=0
        output=model.predict([[ssc_p,hsc_p,degree_p,etest_p,gender_M,workex_Yes]])
        
        if output == 0:
            res_val = "** Sorry you need to work hard! **"
        else:
            res_val = "Congrats! You are Qualified"
        return render_template('index.html', prediction_text=' {}'.format(res_val))
    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run() 
