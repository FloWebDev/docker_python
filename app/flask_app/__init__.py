from flask import Flask, render_template

app = Flask(__name__, static_folder='assets/', template_folder="templates_dir/")

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/test")
def hello_test():
    return render_template('css.html')

@app.errorhandler(404)
def page_not_found(e):
    return "<p>Not Found!</p>", 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
