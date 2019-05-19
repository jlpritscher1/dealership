from sqlalchemy import create_engine,Column,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

    #start with "postgres://" THEN your username:password THEN @"endpoint URL (from AWS)" THEN the name fo your database (popular_movies)
db_string = 'postgres://jlpritscher1:Pm77er..@popular-movie.csrmvxoau93j.us-east-2.rds.amazonaws.com:5432/popular_movies'
db = create_engine(db_string) # Create Connection to database
Base = declarative_base() # setting decalrative_base to a variable named 'Base'

# Creation of Database Models for Object relational Mapper -- AKA "ORM"

class Film(Base):
    __tablename__ = 'films'

    title = Column(String,primary_key = True)
    director = Column(String)
    year = Column(String)

Session = sessionmaker(db)
create_session = Session()

Base.metadata.create_all(db) # grabs hold of 'Base

# create first film table
doctor_strange = Film(title='Doctor Strange',director='Scott Derrickson',year='2016')
black_panther = Film(title='Black Panther',director='Scott Derrickson',year='2016')
create_session.add(black_panther)
create_session.commit()

films = create_session.query(Film)
for film in films:
    print(film.title)

