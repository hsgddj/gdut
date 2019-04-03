from flask import Flask

app = Flask(__name__)

@app.route('/')

def index(): 
    return "Hello, World!  这只是开始!"

app.run(port=8000) 
