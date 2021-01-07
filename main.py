from flask import Flask, render_template
# import requests
# from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/background')
def background():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
