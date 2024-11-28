# model/Hotel.py

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

    # ********** Add a guest to the hotel ***********
    def add_guest(self, guest: Hotelguest) -> None:
        """Adds a guest to the hotel's list if not already present."""
        if guest not in self.__guests:
            self.__guests.append(guest)
            print(f"Added guest: {guest}")
        else:
            print(f"Guest {guest} is already in the hotel.")
