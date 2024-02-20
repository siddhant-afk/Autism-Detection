from flask import render_template,request
from init import app
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
generation_config = {"temperature" : 0.9,"top_p" : 1,"top_k" : 1, "max_output_tokens" :2048 }
bard = genai.GenerativeModel("gemini-pro",generation_config=generation_config)
f = open('lrc copy 2.pkl', 'rb')
model = pickle.load(f)




@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register")
def signup():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/predict", methods = ["POST"])
def predict():

    features_dict = request.form.to_dict()
    country = features_dict.pop('country')
    del features_dict["appusage"]

    # scaler = MinMaxScaler()
    # numerical = ['age']

    # features_df = pd.DataFrame(data = [features_dict],index=[0])
    # features_df[numerical] = scaler.fit_transform(features_df[numerical])
    # features = []
    
    # for key,val in features_dict.items():
    #     features.append(val)
    
    # features = [int(x) for x in features]
   

    features_array = np.array([[int(value) for value in features_dict.values()]])

    # print(features)
    # features = np.array(features)

    prediction = model.predict(features_array)
    print(prediction)

    if prediction[0] == 1:
        result = "Autism detected"
    else:
        result = "Autism not detected"

    focus = bard.generate_content(["Generate a list of all available focus groups for autistic people in india. Omit the heading"])
    therapies =  bard.generate_content(["Generate a list of all available therapies for autistic people in india. Omit the heading"])
    treatments = bard.generate_content(["Generate a list of all available treatments for autistic people in india. Omit the heading"])
    return render_template("result.html",result = result,focus = focus, therapies = therapies, treatments = treatments)


@app.route("/result")
def result():
    return render_template("result.html")

if __name__ =="__main__":
    app.run(debug=True)
    