from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    # name="govind"
    # token=76488
    name=request.args['name']
    token=request.args['token']
    
    return render_template("index.html",name=name,token=token)
app.run(debug=True)
