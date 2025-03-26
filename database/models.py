"""By Théo Régi"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
#-----------------------------------------------------------------------------------------------------
#------------------------------------Models for DB interractions--------------------------------------
#-----------------------------------------------------------------------------------------------------
class PortfolioDB(Base):
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    invested_capital = Column(Float)

    positions = relationship(
        "PositionDB",
        backref="portfolio",
        cascade="all, delete-orphan")

class PositionDB(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    portfolio_id = Column(Integer, ForeignKey('portfolios.id', ondelete='CASCADE'))
    isin = Column(String)
    pru = Column(Float)
    quantity = Column(Float)
    date_achat = Column(Date)
    type = Column(String)
    source = Column(String)

