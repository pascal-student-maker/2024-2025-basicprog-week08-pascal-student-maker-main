from model.Hotelguest import Hotelguest

#testing of data class
guest1 = Hotelguest("Walcarius", "Stijn")
guest2 = Hotelguest("Walcarius", "Stijn")

#check equality
if guest1 == guest2:
    print("Equals!")
else:
    print("Not equals")


gast3 = Hotelguest("Bostyn", "Henk")
gast4 = Hotelguest("Dewitte", "Marie")
guests = [guest1, gast3, gast4]

#equality is also used here
if not guest2 in guests:
    guests.append(guest2)
else:
    print("Guest 2 is already added.")

print(f"Test: {guests}\n")