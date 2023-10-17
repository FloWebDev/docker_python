# import flask module
from flask import Flask, render_template
 
# instance of flask application
app = Flask(__name__, template_folder="tpl")
 
# home route that returns below text
# when root url is accessed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/css")
def css():
    return render_template('css.html')

@app.route("/test")
def test():
    return "<p>Hello, World from test!</p>"

@app.route("/hello")
def hello():
    return "<p>HELLO YOU!!!!!!!!!!!!!!!!<br>!!!!!!!!!!!!!!</p>"

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
 
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)