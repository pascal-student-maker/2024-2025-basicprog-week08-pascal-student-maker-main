from model.Hotel import Hotel
from model.Hotelguest import Hotelguest
from model.HotelRepository import HotelRepository

# Create a hotel instance
hotel_howest = Hotel("Howest")
print(hotel_howest)

# Read guests from the hotel_howest.txt file using the correct method
guests = HotelRepository.read_hotel_guests("doc/hotel_howest.txt")

# Add each guest to the hotel
for guest in guests:
    hotel_howest.add_guest(guest)

# Print information about all hotel guests
hotel_howest.print_info_guests()
