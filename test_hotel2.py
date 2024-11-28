from model.Hotel import Hotel
from model.Hotelguest import Hotelguest
from model.HotelRepository import HotelRepository

hotel_howest = Hotel("Howest")
print(hotel_howest)

guests = HotelRepository.read_guests("doc/hotel_howest.txt")
for guest in guests:
    hotel_howest.add_guest(guest)

hotel_howest.print_info_guests()
