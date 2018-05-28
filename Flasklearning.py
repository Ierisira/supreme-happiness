from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")


@app.route('/<string:name>')
def hello(name):
    name = name.capitalize()
    return f'<h1>Hello, {name}</h1>'


if __name__ == "__main__":
    app.run()
