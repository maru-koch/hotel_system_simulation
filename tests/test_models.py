import unittest

import unittest
from database import Database
from models import Room, Hotel, Booking

class TestModels(unittest.TestCase):
    
    record = {'hotel_id': 1, 'price': 10000, 'capacity': 1}
    Room.hotel_id = 1 
    def test_room_create(self):
        self.assertIsInstance(Room.create(self.record), dict)

    def test_room_hotel(self):
        db = {  1: {'id': 1, 'size': 12, 'booked': True}}
        self.assertEqual(Room.hotel(Room, db), db[1])
        
    def test_booking_create(self):
        record = {'room_id': 1, 'name': 'Champa', 'paid': False}
        returned = Booking.create(record)
        print(returned)
        self.assertIsInstance(returned, dict)

    def test_booking_room(self):
        db = {  1: {'id': 1, 'size': 12, 'booked': True}}
        booking = Booking.room(Room, db)
        self.assertEqual(booking, db[1])

    def test_hotel_create(self):
        name = Database.hotels.insert(name = "DevA_G hotel")
        self.assertEqual(name, {1: {'name': 'palace hotel'}, 2: {'name': 'DevA_G hotel'}} )

        

if __name__ == '__main__':
    unittest.main()