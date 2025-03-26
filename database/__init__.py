"""By Théo Régi"""
from constants import DATABASE_PATH
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
#-----------------------------------------------------------------------------------------------------
#------------------------------------Engine for DB Interractions--------------------------------------
#-----------------------------------------------------------------------------------------------------
engine = create_engine(f'sqlite:///{DATABASE_PATH}')
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
