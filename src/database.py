from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# from src.business import get_conn_str 
from src.api import conn_str

# Create a session to connect to the db
# conn_str = get_conn_str('dev_hybrid')

engine = create_engine(conn_str, echo=True) 
Session = sessionmaker(bind=engine)


# Create instance of Base class which does decarative mapping
Base = declarative_base() 

# Create table schema
class AthleteTable(Base):
    __tablename__ = "athlete"

    athlete_id = Column(Integer, Sequence("athlete_user_id_seq"), primary_key=True)
    username = Column(String(50))
    team = Column(String(50))

    def __repr__(self): # returns info in nice formatting
        return "<User(athlete_id='%s',username='%s', team='%s')>" % (
            self.athlete_id,
            self.username,
            self.team,
        )


if __name__ == '__main__':
    # Connect to db and create table
    Base.metadata.create_all(engine)

    # Create instance of User class and add to pending commits
    kaja_user = AthleteTable(username="kaja", team="maroon")
    session = Session()
    session.add(
        kaja_user
    ) 

    # search db for Kaja
    selected_athlete = session.query(AthleteTable).filter_by(username="kaja").first()
    print(selected_athlete)

    # commit to db
    session.commit()