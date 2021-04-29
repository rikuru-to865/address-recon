from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/")
def index():
    print(app.logger())
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')