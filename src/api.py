import os 
import pdb
from typing import Union, List
from http import HTTPStatus

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
from fastapi import FastAPI, Request 
import uvicorn 

from src.classes import Response
import src.business as b
from src.database import User

# CONSTANTS
ENV = 'dev_local'
# ENV = os.getenv("ENV")
conn_str = b.get_conn_str(ENV)

# INSTANTIATIONS 
app = FastAPI() 
engine = create_engine(conn_str, echo=True) 
Session = sessionmaker(bind=engine) 


# ENDPOINTS 
@app.get("/")
def read_landing():
    return 'Hello World'


@app.get("/health")
def read_health():
    return {'API Status': HTTPStatus.OK}


@app.get('/users')
def read_users():
    """
    Get all data from the atomic_winter postgres db 'users' table
    """
    try:
        with Session() as session:
            user_data = session.query(User).all()
    except Exception as e:
        return Response(status_code=500, error_message=e)
    return Response(body={'users':user_data})
