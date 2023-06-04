from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, text
from database import load_jobs_from_db

app = Flask(__name__)



@app.route("/")
def hello_jovian():
    jobs=load_jobs_from_db()
    return render_template('home.html', jobs=jobs,
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001)#debug=True)