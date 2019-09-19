from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def x():
    return render_template('inex.html')
@app.route("/home")
def y():
    return render_template('home.html')
@app.route("/contact")
def z():
    return("school id 2")
if(__name__=="__main__"):
    app.run(debug=True)
