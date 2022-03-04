from .model import Model
from database import Database

class Hotel(Model):
    _id = None
    name = None

    @classmethod
    def create(cls, record):
        # Requirements:
        #   - The record argument will always be a dictionary representing a database record
        #   - Assign values from the record dictionary to the corresponding model attributes
        cls.name = record
        return Database.hotels.insert(name = cls.name)

       


