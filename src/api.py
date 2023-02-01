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
from src.database import Athlete

# CONSTANTS
ENV = 'dev_hybrid'
try:    
    ENV = os.getenv("ENV")
except:
    pass 
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


@app.get('/athlete')
def read_users():
    """
    Get all data from the atomic_winter postgres db 'athlete' table
    """
    try:
        with Session() as session:
            user_data = session.query(Athlete).all()
    except Exception as e:
        return Response(status_code=500, error_message=e)
    return Response(body={'athletes':user_data})
