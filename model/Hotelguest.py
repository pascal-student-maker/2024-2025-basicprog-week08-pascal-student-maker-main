class Hotelguest:
    def __init__(self, parlastname: str, parfirstname: str, parbalance: float = 0.0, par_checked_in: bool = True) -> None:
        self.lastname = parlastname
        self.firstname = parfirstname
        self.balance = parbalance
        self.is_checked_in = par_checked_in

    # ********** property lastname - (setter/getter) ***********
    @property
    def lastname(self) -> str:
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
        return self.__firstname

    @firstname.setter
    def firstname(self, value: str) -> None:
        if value != "":
            self.__firstname = value
        else:
            self.__firstname = "Unknown"

    # ********** property balance - (setter/getter) ***********
    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> None:
        if isinstance(value, (int, float)) and value >= 0:
            self.__balance = float(value)  # Ensure it is always a float
        else:
            self.__balance = 0.0

    # ********** property is_checked_in - (setter/getter) ***********
    @property
    def is_checked_in(self) -> bool:
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
            return f"Hotelguest: {self.firstname} {self.lastname} - Checked in: {self.is_checked_in} (balance {self.balance:.2f} euro)"
        else:
            return f"X: {self.firstname} {self.lastname.upper()}"
