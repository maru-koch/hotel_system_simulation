from hotel_system import HotelSystem, Input
from database import table

class Main(HotelSystem, Input):

    def start(self):
        while True:
            user = self.select_user()
            if user == 'admin':
                task = self.admin_task()
                if task == 'register':
                    hotel_name = self.add_hotel()
                    self.register_hotel(hotel_name)

                elif task == 'add_room':
                    room = self.room_details()
                    try:
                        hotel_id, price, capacity = room
                    except TypeError:
                        print("You missed a value. please Try again")
                    else:
                        self.add_room(hotel_id = hotel_id, price = price, capacity = capacity)
                    
            elif user == 'manager':
                info = self.room_info()
                if info == 'get_room':
                    room_id = self.room_id()
                    self.get_room(room_id)

                elif info == 'book_room':
                    room, name, paid = self.booking_details()
                    self.book_room(room_id = room, name = name, paid = paid)


if __name__=='__main__':
    from database import Database
    db = Database()
    HoSys = Main(db)
    HoSys.start()