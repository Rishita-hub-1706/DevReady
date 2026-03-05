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
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)



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
            flash("Invalid ID or Password", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/hr_dashboard", methods=["GET","POST"])
def hr_dashboard():

    if request.method == "POST":
        task_title = request.form["task"]

        new_task = Task(title=task_title)
        db.session.add(new_task)
        db.session.commit()

    tasks = Task.query.all()

    return render_template("hr_dashboard.html", tasks=tasks) 

@app.route("/employee_dashboard")
def employee_dashboard():

    tasks = Task.query.all()

    completed = Task.query.filter_by(completed=True).count()
    total = Task.query.count()

    progress = 0

    if total > 0:
        progress = int((completed/total)*100)

    return render_template(
        "employee_dashboard.html",
        tasks=tasks,
        progress=progress
    )

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info") 
    return redirect(url_for("login"))

@app.route("/complete_task/<int:task_id>", methods=["POST"])
def complete_task(task_id):

    task = Task.query.get(task_id)

    task.completed = not task.completed

    db.session.commit()

    return redirect(url_for("employee_dashboard"))

@app.route("/logout")
def logout():
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)