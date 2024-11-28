from dataclasses import dataclass

@dataclass
class Birthdate:
    _day: int
    _month: int
    _year: int

    # Getter and setter for day
    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value: int):
        if 1 <= value <= 31:
            self._day = value
        else:
            raise ValueError("Day must be between 1 and 31.")

    # Getter and setter for month
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value: int):
        if 1 <= value <= 12:
            self._month = value
        else:
            raise ValueError("Month must be between 1 and 12.")

    # Getter and setter for year
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        if value > 0:
            self._year = value
        else:
            raise ValueError("Year must be a positive integer.")

    # Constructor automatically created by @dataclass
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    # Method to represent the date as a string "day/month/year"
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

    # Equality check for comparing two Birthdate objects
    def __eq__(self, other): 
        if isinstance(other, Birthdate):
            return (self.day == other.day) and (self.month == other.month) and (self.year == other.year)
        return False

    # Developer-friendly representation of the object
    def __repr__(self):
        return f"Birthdate(day={self.day}, month={self.month}, year={self.year})"
