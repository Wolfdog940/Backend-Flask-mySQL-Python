from flask import Flask

#creamos instancia de flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Flask app"


if __name__ =="__main__":
    app.run(debug=True,port=5000)