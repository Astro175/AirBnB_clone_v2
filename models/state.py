#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import relationship
class State(BaseModel):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if HBNB_TYPE_STORAGE == 'db':
        cities = relationship("City", back_populates="state",
                cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            list_cities= []

            for city in models.storage.all(City):
                if city.state_id = self.id:
                    list_cities.append(city)

            return list_cities

