from flask import Flask, render_template,request
import json
import requests
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/address",methods=["POST"])
def address():
    info = request.get_data()
    requests.post(os.getenv("webhook"),"content="+info,headers={'content-type',
      'application/x-www-form-urlencoded;charset=UTF-8'})

if __name__ == "__main__":
    app.run(host='0.0.0.0')