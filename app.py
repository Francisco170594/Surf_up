from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route("/about")
def about():
    print("Server received request for 'about' page...")
    return "Welcome to my 'about' page"

