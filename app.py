from flask import Flask, render_template

app = Flask(__name__)

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