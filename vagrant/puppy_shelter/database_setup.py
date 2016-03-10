import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy import Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(80))
    zipCode = Column(Integer)
    website = Column(String(250))
    maximum_capacity = Column(Integer, nullable=False)
    current_occupancy = Column(Integer)


class Adoption(Base):
    __tablename__ = 'association'
    puppy_id = Column(Integer, ForeignKey('puppy.id'), primary_key=True)
    adopter_id = Column(Integer, ForeignKey('adopter.id'), primary_key=True)
    date = Column(Date)
    puppy = relationship("Puppy", back_populates="adopters")
    adopter = relationship("Adopter", back_populates="puppies")


class Adopter(Base):
    __tablename__ = 'adopter'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    last_name = Column(String(80))
    puppies = relationship("Adoption", back_populates="adopter")


class Puppy(Base):
    __tablename__ = 'puppy'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    date_of_birth = Column(Date)
    gender = Column(String(10), nullable=False)
    weight = Column(Float)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    puppy_profile = relationship("PuppyProfile",
                                 uselist=False,
                                 back_populates="puppy")
    adopters = relationship("Adoption", back_populates="puppy")


class PuppyProfile(Base):
    __tablename__ = 'puppy_profile'

    id = Column(Integer, primary_key=True)
    picture_url = Column(String(250))
    description = Column(String(250))
    special_needs = Column(String(250))
    puppy_id = Column(Integer, ForeignKey('puppy.id'))
    puppy = relationship('Puppy', back_populates='puppy_profile')


engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)
