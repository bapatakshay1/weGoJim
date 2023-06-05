from flask import Flask, render_template, jsonify, request
from sqlalchemy import create_engine, text
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)



@app.route("/")
def hello_jovian():
    jobs=load_jobs_from_db()
    return render_template('home.html', jobs=jobs,
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  jobs=load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def showJob(id):
  job=load_job_from_db(id)
  if not job:
     return "Not Found", 404
  return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html', 
                         application=data,
                         job=job)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)