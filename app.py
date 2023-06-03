from flask import Flask, render_template, request, session, redirect, jsonify
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)
JOBS =[{
    'id': 1,
    'title': "data Analyst",
    'location': 'Bengalru, India',
    'salary': 'Rs, 1,00,000' 
},
{'id': 2,
    'title': "data scientist",
    'location': 'mumbai, India',
    'salary': 'Rs, 1,02340,000' 
},
{'id': 3,
    'title': "principal data scientist",
    'location': 'delhi india',
},
]
@app.route("/")
def hello_world():
    return render_template('index.html', jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    # Set the host and port
    host = '0.0.0.0'  # Change to your desired host, e.g., 'localhost'
    port = 5001  # Change to your desired port number

    # Run the Flask application
    app.run(host=host, port=port)