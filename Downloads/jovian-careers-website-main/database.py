from sqlalchemy import create_engine, text
#pip install pymysql
#pip install sqlalchemy

db_connection_string="mysql+pymysql://rik2xhp6wye970ywuaac:pscale_pw_eTfYHGqNEM43XMFYtHFEg52PWTOMSpZ6oFqeJfKNXLs@aws.connect.psdb.cloud/wegojim?charset=utf8mb4"

engine = create_engine(db_connection_string,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    }
)


def load_jobs_from_db():
   with engine.connect() as conn:
    result=conn.execute(text("select * from jobs"))
    jobs=[]
    col_names=result.keys()
    for row in result:
        jobs.append(dict(zip(col_names, row)))
    return jobs

def load_job_from_db(id): 
    with engine.connect() as conn: 
        result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}") )
    rows = result.all()
    if len(rows) == 0:
        return None
    else:
        return rows[0]._asdict()
    

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

        conn.execute(query, {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],
            'resume_url': data['resume_url']
        })