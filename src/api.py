import os 
import pdb
from typing import Union, List
from http import HTTPStatus

from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
from fastapi import FastAPI, Request 
import uvicorn 

from src.classes import Response, Athlete
import src.business as b
from src.database import AthleteTable

# CONSTANTS
ENV = b.get_env('dev_hybrid')
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
def read_users(username:str=None):
    """
    Get all data from the atomic_winter postgres db 'athlete' table OR if query arg included affirm if athlete in db - note: not good REST API but good as example
    """
    try:
        with Session() as session:
            user_data:List[Athlete] = session.query(AthleteTable).all() 
    except Exception as e:
        return Response(status_code=500, error_message=e)
    if username:
        for user in user_data:
            if user.username == username:
                return Response(body={f'{username} registered': True})
        return Response(body={f'{username} registered': False})
    return Response(body={'athletes':user_data})

@app.post('/athlete')
def create_athlete(athlete: Athlete):
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