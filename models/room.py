from .model import Model
from .hotel import Hotel
from database import Database

class Room(Model):
    _id = None
    hotel_id = None
    price = None
    capacity = None

    @classmethod
    def create(cls, record):
        # Requirements:
        #   - The record argument will always be a dictionary representing a database record
        #   - Assign values from the record dictionary to the corresponding model attributes

        cls.hotel_id = record['hotel_id']
        cls.price = record['price']
        cls.capacity = record['capacity']

        room = Database.rooms

    
       
        db = Database.hotels.data
        hotels = cls.hotel(cls, db)
        print(hotels, db)

        return room.insert(      
                        hotel_id = record['hotel_id'], 
                        price = cls.price, 
                        capacity = cls.capacity
                        
                        )

    def hotel(self, db):
        # Requirements:
        #   - Select hotels from the database that has the hotel_id set on this model as self.hotel_id
        #   - Return None if query results is empty
        #   - Otherwise,
        #   - Return a Hotel model instance by calling the model's create method with the first record in the query results

        for key in db.keys():
            if key == self.hotel_id:
                return db[key] 
        return None

        