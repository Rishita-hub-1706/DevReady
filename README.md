# DevReady – Employee Onboarding Task Tracker

DevReady is a simple web application built with Flask that helps HR assign onboarding tasks to employees and allows employees to track and complete those tasks.
LIVE SERVER:
https://devready11.onrender.com
## Features

* HR can add onboarding tasks
* HR can delete tasks
* Employees can view assigned tasks
* Employees can mark tasks as completed
* Progress bar showing task completion percentage
* Separate dashboards for HR and Employees
* Login system with password hashing

## Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* HTML
* CSS

## Project Structure

```
project/
│
├── app.py
├── requirements.txt
├── Procfile
│
├── templates/
│   ├── login.html
│   ├── hr_dashboard.html
│   └── employee_dashboard.html
│
└── static/
    ├── style.css
    └── favicon.ico
```

## Installation

1. Clone the repository

```
git clone https://github.com/your-username/devready.git
cd devready
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
python app.py
```

4. Open in browser

```
http://127.0.0.1:5000
```

## Deployment

This project can be deployed easily using Render with:

```
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

## Author

Built as a learning project using Flask.
