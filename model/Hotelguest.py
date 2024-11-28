class Hotelguest:
    def __init__(self, parlastname: str, parfirstname: str, parbalance: int = 0, par_checked_in: bool = True) -> None:
        self.lastname = parlastname
        self.firstname = parfirstname
        self.balance = parbalance
        self.is_checked_in = par_checked_in

    # ********** property lastname - (setter/getter) ***********
    @property
    def lastname(self) -> str:
        """ The lastname property. """
        return self.__lastname
    
    @lastname.setter
    def lastname(self, value: str) -> None:
        if value != "":
            self.__lastname = value
        else:
            self.__lastname = "Unknown"
    
    # ********** property firstname - (setter/getter) ***********
    @property
    def firstname(self) -> str:
        """ The firstname property. """
        return self.__firstname
    
    @firstname.setter
    def firstname(self, value: str) -> None:
        if value != "":
            self.__firstname = value
        else:
            self.__firstname = "Unknown"
    
    # ********** property balance - (setter/getter) ***********
    @property
    def balance(self) -> int:
        """ The balance property. """
        return self.__balance
    
    @balance.setter
    def balance(self, value: float) -> None:
        if isinstance(value, float) and value >= 0:
            self.__balance = value
        else:
            self.__balance = 0
    
    # ********** property is_checked_in - (setter/getter) ***********
    @property
    def is_checked_in(self) -> bool:
        """ The is_checked_in property. """
        return self.__is_checked_in
    
    @is_checked_in.setter
    def is_checked_in(self, value: bool) -> None:
        if isinstance(value, bool):
            self.__is_checked_in = value
        else:
            self.__is_checked_in = False

    # ********** String Representation ***********
    def __str__(self) -> str:
        if self.is_checked_in:
            return f"Hotelguest: {self.firstname} {self.lastname} - Checked in: {self.is_checked_in} (balance {self.balance} euro)"
        else:
            return f"X: {self.firstname} {self.lastname.upper()}"

    # ********** Representation for Debugging ***********
    def __repr__(self) -> str:
        return (f"Hotelguest(lastname='{self.lastname}', firstname='{self.firstname}', "
                f"balance={self.balance}, is_checked_in={self.is_checked_in})")

    # ********** Equality Method ***********
    def __eq__(self, other) -> bool:
        """Check if two hotel guests are equal based on lastname and firstname."""
        if isinstance(other, Hotelguest):
            return self.lastname.lower() == other.lastname.lower() and self.firstname.lower() == other.firstname.lower()
        return False

    # ********** Membership Method ***********
    def __contains__(self, guest_list) -> bool:
        """Check if this guest is already in a list of guests."""
        return any(self == guest for guest in guest_list)
