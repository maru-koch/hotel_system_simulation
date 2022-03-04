from .room import Room
from .model import Model

from database import Database


class Booking(Model):
    _id = None
    room_id = None
    name = None
    paid = None

    @classmethod
    def create(cls, record):
        # Requirements:
        #   - The record argument will always be a dictionary representing a database record
        #   - Assign values from the record dictionary to the corresponding model attributes

        cls.room_id = record['room_id']
        cls._name = record['name']
        cls.paid = record['paid']

        bookings = Database.bookings
        # bookings.insert(room_id = cls.room_id, name = cls.name, paid = cls.paid)
        booking = Database.bookings.data
        cls.room(cls, booking)
        # if room[cls.room_id]['booked']:
        #     print(f"Room {cls.room_id} is already booked by another customer")
        # else:
        
        room = Database.rooms.data
        room[record['room_id']]['booked'] = True

        return bookings.insert(room_id = record['room_id'], name = record['name'], paid = record['paid'])

    def room(self, db):
        # Requirements:
        #   - Select rooms from the database that has the room id set on this model as self.room_id
        #   - Return None if query results is empty
        #   - Otherwise,
        #   - Return a Room model instance by calling the model's create method with the first record in the query results

        for id in db.keys():
            if id == Booking.room_id:
                return db[id]
        return None
