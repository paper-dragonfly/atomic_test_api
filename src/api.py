import os 
import pdb
from typing import Union, List
from http import HTTPStatus

import uvicorn 
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
from fastapi import FastAPI, Request
#adding cors headers
from fastapi.middleware.cors import CORSMiddleware
 

from src.classes import Response, AthletePostSchema
import src.business as b
from src.database import AthleteTable

# CONSTANTS
ENV = b.get_env('dev_hybrid')
conn_str = b.get_conn_str(ENV)
# conn_str = os.getenv('conn_str')

# INSTANTIATIONS 
app = FastAPI() 
engine = create_engine(conn_str, echo=True) 
Session = sessionmaker(bind=engine) 

#add cors urls and middleware
origins = [
    'http://localhost:3000',
    'localhost:3000' ]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ['*']
    )

# ENDPOINTS 
@app.get("/")
def read_landing():
    return 'Hello World'


@app.get("/health")
def read_health():
    return {'API Status': HTTPStatus.OK}


@app.get('/athlete')
def read_users(username:str=None):
    """
    Get all data from the atomic_winter postgres db 'athlete' table OR if query arg included affirm if athlete in db - note: not good REST API but good as example
    """
    try:
        with Session() as session:
            user_data:List[AthletePostSchema] = session.query(AthleteTable).all() 
    except Exception as e:
        return Response(status_code=500, error_message=e)
    if username:
        for user in user_data:
            if user.username == username:
                return Response(body={f'{username} registered': True})
        return Response(body={f'{username} registered': False})
    return Response(body={'athletes':user_data})

@app.post('/athlete')
def create_athlete(athlete: AthletePostSchema): #take in post info - parse to confirm matches expected AthletePostSchema params
    """
    Add athlete to db, return ID
    """
    try:
        with Session() as session:
            new_user = AthleteTable(username=athlete.username, team=athlete.team)
            session.add(new_user) 
            new_id = session.query(AthleteTable.athlete_id).filter_by(AthleteTable.username==athlete.username)
    except Exception as e:
        return Response(status_code=500, error_message=e)
    return Response(body={'new_id':new_id})