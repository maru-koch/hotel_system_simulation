import unittest

import unittest
from database import Database
from hotel_system import HotelSystem

class TestHotelSystem(unittest.TestCase):
    hotel_sys = HotelSystem(Database)

    def test_register_hotel(self):
        register = self.hotel_sys.register_hotel('palace hotel')
        self.assertEqual(register, {1:{'name':'palace hotel'}})
        
    def test_add_room(self):
        room = self.hotel_sys.add_room(room_id=1, price = 5000, capacity = 1)
        self.assertIsInstance(room, dict)

    #: error used when room id is not found
    def test_get_room(self):
        with self.assertRaises(Exception):
             HotelSystem(Database).get_room(1)
    
    #: fixed assertion error
    def test_book_room(self):
        booked = self.hotel_sys.book_room(room_id= 1, name = 'Munero', paid = True) 
        self.assertIsInstance(booked, dict)

    def test_add_room(self):
        room = self.hotel_sys.add_room(hotel_id=1, price = 5000, capacity = 1)
        self.assertIsInstance(room, dict)

if __name__ == '__main__':
    unittest.main()