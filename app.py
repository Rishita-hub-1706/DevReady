from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "dev_ready_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devready.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        employee_id = request.form.get("employee_id")
        password = request.form.get("password")

        user = User.query.filter_by(employee_id=employee_id).first()

        # 1. Use check_password_hash instead of ==
        if user and check_password_hash(user.password, password):
            session["role"] = user.role.lower()
            session["user_id"] = user.id # Good habit to store this too
            
            if session["role"] == "hr":
                return redirect(url_for("hr_dashboard"))
            else:
                return redirect(url_for("employee_dashboard"))
        else:
            # 2. This helps you see if the login failed
            flash("Invalid Employee ID or Password", "error")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/hr_dashboard")
def hr_dashboard():
    
    if "role" in session and session["role"] == "hr":
        return render_template("hr_dashboard.html")
    return redirect(url_for("login")) 

@app.route("/employee_dashboard")
def employee_dashboard():
    if "role" in session and session["role"] == "employee":
        return render_template("employee_dashboard.html")
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info") # 👈 Add this
    return redirect(url_for("login"))




if __name__ == "__main__":
    app.run(debug=True)