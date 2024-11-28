from dataclasses import dataclass
from model.Hotelguest import Hotelguest

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.__guests = []  # Private list to store hotel guests

    # ********** property name - (setter/getter) ***********
    @property
    def name(self) -> str:
        """The name property."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Setter for the hotel name with validation."""
        if value.strip():  # Ensures the name is not an empty string or only spaces
            self.__name = value
        else:
            raise ValueError("Hotel name cannot be empty.")

    # ********** property guests - (getter only) ***********
    @property
    def guests(self) -> list:
        """The guests property. Returns the list of guests."""
        return self.__guests

    def __str__(self) -> str:
        """String representation of the Hotel."""
        return f"Hotel: {self.name}"

    def check_in(self, lastname: str, firstname: str) -> None:
        """Checks in a guest into the hotel."""
        # Create a new hotel guest object
        new_guest = Hotelguest(lastname, firstname)
        
        # Check if the guest is already in the list
        if new_guest in self.__guests:
            print(f"Error: {new_guest} is already checked in.")
        else:
            # Add the new guest to the list and update their status
            self.__guests.append(new_guest)
            new_guest.is_checked_in = True
            print(f"Checked in correctly: {new_guest}")

    def print_info_guests(self) -> None:
        """Prints detailed information about all hotel guests."""
        print(f"Hotel: {self.name}")
        print(f"Guests ({len(self.__guests)} total):")
        for guest in self.__guests:
            print(f"- {guest}")
