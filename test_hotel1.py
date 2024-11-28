from model.Hotel import Hotel
from model.Hotelguest import Hotelguest

hotel_howest = Hotel("Howest")
print(hotel_howest)
hotel_howest.check_in("Claerhout", "Joerie")
hotel_howest.check_in("Dewitte", "Marie")
hotel_howest.print_info_guests()

hotel_howest.check_out("Dewitte","Marie")
hotel_howest.check_out("De Gelas", "Johan")
hotel_howest.print_info_guests()

hotel_howest.guests[0].balance = 75.5             #Joerie drunk a lot last night
hotel_howest.check_out("Claerhout", "Joerie")    #first try
print("\nJoerie pays its debt.")
hotel_howest.balance_paid_by_guest("Claerhout", "Joerie")
hotel_howest.check_out("Claerhout", "Joerie")    #second try