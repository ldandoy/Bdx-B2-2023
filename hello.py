from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template(
        'hello.html',
        name="Loïc DANDOY"
    )


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')


app.run(debug=True, use_reloader=True)
