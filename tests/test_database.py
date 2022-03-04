
import unittest
from database import Database

class TestDatabase(unittest.TestCase):

    def test_room_insert(self):
        room = Database.rooms.insert(hotel_id = 1, price = 10000, capacity = 1)
        self.assertDictEqual(room, {1: {'hotel_id': 1, 'price': 10000, 'capacity': 1}})
    
    def test_booking_insert(self):
        booking = Database.bookings.insert(room_id = 1, name = 'Chief', paid = True)
        self.assertDictEqual(booking, {1: {'room_id': 1, 'name': 'Chief', 'paid': True}})
    
    #: returns None if no hotel records matches the given condition
    def test_select_hotel(self):
        condition = Database.hotels.select(name = 'Chief')
        self.assertEqual(condition, [])
    
    #: returns None if no hotel records matches the given condition
    def test_select_booking(self):
        booking = Database.bookings
        booking.data = {1:{'hotel_id': 1, 'price': 10000, 'capacity': 1}, 2: {'hotel_id': 1, 'price': 10000, 'capacity': 1}}
        selected = booking.select(room_id = 1, name = 'Chief', paid = True)
        self.assertEqual(selected,[])
    
    def test_except(self):
        with self.assertRaises(Exception):
            Database.hotels.insert("Candy's Motel")

    

if __name__ == '__main__':
    unittest.main()