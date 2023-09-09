import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50))
    email = Column(String(50), unique=True, nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    height = Column(String(50), nullable=False)
    mass = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    diameter = Column(String(50), nullable=False)
    rotation_period = Column(String(50), nullable=False)
    orbital_period = Column(String(50), nullable=False)
    gravity = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    surface_water = Column(String(50), nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    starship_class = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    cost_in_credits = Column(String(50), nullable=False)
    length = Column(String(50), nullable=False)
    crew = Column(String(50), nullable=False)
    passengers = Column(String(50), nullable=False)
    max_atmosphering_speed = Column(String(50), nullable=False)
    hyperdrive_rating = Column(String(50), nullable=False)
    MGLT = Column(String(50), nullable=False)
    cargo_capacity = Column(String(50), nullable=False)
    consumables = Column(String(50), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))
    user = relationship('User')
    character = relationship('Characters')
    planet = relationship('Planets')
    starships = relationship('Starships')

    def to_dict(self):
        return {}


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e