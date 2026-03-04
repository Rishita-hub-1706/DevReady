from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devready.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        employee_id = request.form.get("employee_id")
        password = request.form["password"]

        user = User.query.filter_by(
            employee_id=employee_id,
            password=password
        ).first()

        if user:
            if user.role == "hr":
                return redirect(url_for("hr_dashboard"))
            else:
                return redirect(url_for("employee_dashboard"))
        else:
            return "Invalid credentials"

    return render_template("login.html")

@app.route("/hr_dashboard")
def hr_dashboard():
    return "Welcome HR Dashboard"

@app.route("/employee_dashboard")
def employee_dashboard():
    return "Welcome Employee Dashboard"




if __name__ == "__main__":
    app.run(debug=True)