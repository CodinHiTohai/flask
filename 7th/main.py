from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")

def hello_world():
    marks={
        "govind":55,
        "saurabh":88,
        "shubham":93,
        "sumit":23,
        "devjyoti":83,
        "ashish":11
    }
    return render_template("index.html",marks=marks)
app.run(debug=True)