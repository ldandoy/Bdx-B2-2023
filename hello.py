from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, func

from models import Data

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

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
    datas = db.session.query(Data.ville, func.count(Data.id)).group_by(Data.ville).limit(10).all()

    return render_template('dashboard.html', datas=datas)


app.run(debug=True, use_reloader=True)
