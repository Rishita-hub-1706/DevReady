from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devready.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/employee")
def employee_dashboard():
    return render_template("employee_dashboard.html")

@app.route("/hr")
def hr_dashboard():
    return render_template("hr_dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)