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
 
