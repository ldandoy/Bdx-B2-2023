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
    datas = [{'label': 'Red', 'vote': 12}, {'label': 'Blue', 'vote': 19}, {'label': 'Yellow', 'vote': 3},
             {'label': 'Green', 'vote': 5}, {'label': 'Purple', 'vote': 2}, {'label': 'Orange', 'vote': 3}]

    return render_template('dashboard.html', datas=datas)


app.run(debug=True, use_reloader=True)
