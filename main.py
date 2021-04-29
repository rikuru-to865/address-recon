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
    main_content = {
  "content": info
  }
    requests.post(os.getenv("webhook"),main_content)

if __name__ == "__main__":
    app.run(host='0.0.0.0')