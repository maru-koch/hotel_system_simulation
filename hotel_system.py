from models import Room, Hotel, Booking
from database import Database

class HotelSystem:
    def __init__(self, db):
        self.index = 1
        self.db = db
        self.room = db.rooms.data
        self.hotel = db.hotels.data


    def register_hotel(self, name):
        # Requirements:
        #   - Insert new hotel record into the database
        #   - Return a Hotel model instance by calling the model's create method with the query result
        return Hotel.create(name)
        
    def add_room(self, **params):
        # Requirements:
        #   - Insert new room record into the database
        #   - Return a Room model instance by calling the model's create method with the query result
        return Room.create({'hotel_id': params['hotel_id'], 'price': params['price'], 'capacity': params['capacity']})
    
           

    def get_room(self, room_id):
        # Requirements:
        #   - Select a room with the room_id argument from the database
        #   - Return None if query results is empty
        #   - Otherwise,
        #   - Return a Room model instance by calling the model's create method with the first record in the query results
       
   
        for id in self.room.keys():
            if id == room_id:
                print(f"\t Hotel: {self.hotel[self.room[id]['hotel_id']]['name']}, -- Room: {1} \n\t Price: {self.room[id]['price']} \n\t Capacity: {self.room[id]['capacity']}")
                return self.room[id]
            else:
                pass
        

        return None

    def book_room(self, **params):
        # Requirements:
        #   - Insert new booking record into the database
        #   - Return a Booking model by calling the model's create method instance with the query result

        # if self.room:
        #     record = {'room_id': params['room_id'], 'customer': params['customer'], 'paid': params['paid']}
        #     return Booking.create(record)
        # else:
        #     print('No available room')
        #     return "No available room"
        
        record = {'room_id': params['room_id'], 'name': params['name'], 'paid': params['paid']}
        return Booking.create(record)

class Input():
    def select_user(self):
        users = {1:'admin', 2:'manager'}
        while True:
            try:
                response =int(input("Select User (1 - Admin or 2 - Manager): "))
                user = users[response]
            except Exception:
                print("Please only Enter 1 or 2.")
            else:
                return user
    
    def admin_task(self):
        operations = {1:'register', 2: 'add_room'}
        try:
            operate = int(input("Operations: \n1.  Register Hotel  \n2.  Add room details: "))
            operation = operations[operate]

        except (ValueError, KeyError):
            print("Enter 1 or 2")
        else:
           
            return operation

    def add_hotel(self):
        try:
            name = input("Hotel Name: ")
        except ValueError:
            print("Hotel name must be a string")
        else:
            return name
    
    def room_details(self):
        try:
            hotel_id = int(input("Hotel_id: "))
            price = int(input("Price: "))
            capacity = int(input("Capacity: "))
        except ValueError:
            print("Enter the appropriate Values")
        else:
            return hotel_id, price, capacity

    def room_info(self):
        try:
            infos = {1:'get_room', 2:'book_room'}
            info = int(input("Operations: \n1.    Get room Information    \n2.    Book a room: "))
            info = infos[info]
        except ValueError:
            print("No letters or words. Enter 1 or 2")
        except KeyError:
            print("Only enter 1 0r 2")
        else:
            return info

    def booking_details(self):
        try:
            room_id = int(input("Room Id: "))
            customer = input("Customer's name: ")
            paid = input("Paid? True or False: ")
        except ValueError:
            print("Enter the appropriate Values")
        else:
            print(room_id, customer, paid)
            return room_id, customer, paid

    def room_id(self):
        try:
            id = int(input("Enter room Id: "))
        except ValueError:
            print("Enter the appropriate Values")
        else:
            return int(id)

    


