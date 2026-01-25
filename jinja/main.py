from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks={
        "john":45,
        "shubham":33,
        "sneha":35,
        "devjyoti":88,
        "ashish=sh":83,
        "goivnd":99
    }
    return render_template("index.html",marks=marks)
app.run(debug=True)