import calendar
import datetime

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    day = calendar.weekday(now.year,now.month,now.day)
    day = calendar.day_name[day]
    return render_template("index.html",day = day)

@app.route("/hello",methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html",name=name)