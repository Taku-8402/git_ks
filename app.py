from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/circle")
def circle():
    return render_template("circle.html")

@app.route("/circle_ans")
def circle_ans():
    s = request.args.get("s")
    a = int(s)**2*3.14
    return render_template("circle_ans.html",a=a)
    
if __name__ == "__main__":
    app.run(debug=True)