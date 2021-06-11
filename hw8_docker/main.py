from flask import Flask

app = Flask(__name__)


@app.route("/")
def start():
    return "Start page"


@app.route('/home')
def home():
    return "This is Homepage"


@app.route('/news')
def newsp():
    return "News Hello Andriy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
