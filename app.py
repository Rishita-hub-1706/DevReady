from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devready.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/employee")
def employee_dashboard():
    return render_template("employee_dashboard.html")

@app.route("/hr")
def hr_dashboard():
    return render_template("hr_dashboard.html")

with app.app_context():
    if not User.query.filter_by(employee_id="HR001").first():
        hr = User(employee_id="HR001", password="hr123", role="hr")
        emp = User(employee_id="EMP001", password="emp123", role="employee")
        db.session.add(hr)
        db.session.add(emp)
        db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)