import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

def generate_dsn(path): 
    # return a string in the format of:
    path = "postgresql://sgwie:gHks7246@localhost/homework08"
    return path; 

def get_session(dsn): 
    engine = create_engine(dsn, echo=True)
    Session = sessionmaker(engine)
    #  return a SQLAlchemy session
    session = Session()
    return session; 

class Eatery(): 
    __tablename__ = 'eatery'
    
    eatery_id = Column('eatery_id', Integer, primary_key=True)
    name = Column('name', String)
    location = Column('location', String)
    park_id = Column('park_id', String) 
    start_date = Column('start_date', Date)
    end_date = Column('end_date', Date) 
    description = Column('description', String)
    permit_number = Column('permit_number', String)
    phone = Column('phone', String) 
    website = Column('website', String)
    type_name = Column('type_name', String)

    def __repr__(self):
        return f'{self.eatery_id}: {self.start_date} to {self.end_date} - {self.type_name} - {self.location} - {self.park_id} - {self.type_name} - {self.description} - {self.phone} - {self.website} - {self.permit_number}'
    
    def __str__(self):
        return self.__repr__()