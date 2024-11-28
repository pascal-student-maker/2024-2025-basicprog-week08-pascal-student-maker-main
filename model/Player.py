from model.Birthdate import Birthdate  # Make sure Birthdate is imported

class Player:
    # Public class attributes
    team_name = "unknown team"
    __number_goals_team = 0  # Private class attribute

    def __init__(self, parlastname: str, parfirstname: str, partype: str, parvalue: int = 0, birthdate: Birthdate = None) -> None:
        self.lastname = parlastname
        self.firstname = parfirstname
        self.value_player = parvalue
        self.type = partype
        # Check if a birthdate is passed, otherwise use a default value
        self.birthdate = birthdate if birthdate else Birthdate(1, 1, 1900)
        self.__goals_player = 0

    # ********** property lastname - (setter/getter) ***********
    @property
    def lastname(self) -> str:
        return self.__lastname
    
    @lastname.setter
    def lastname(self, value: str) -> None:
        self.__lastname = value if isinstance(value, str) and value else "unknown"

    # ********** property firstname - (setter/getter) ***********
    @property
    def firstname(self) -> str:
        return self.__firstname
    
    @firstname.setter
    def firstname(self, value: str) -> None:
        self.__firstname = value if isinstance(value, str) and value else "unknown"

    # ********** property value_player - (setter/getter) ***********
    @property
    def value_player(self) -> int:
        return self.__value_player
    
    @value_player.setter
    def value_player(self, value: int) -> None:
        self.__value_player = value if isinstance(value, int) and value >= 0 else -1

    # ********** property type - (setter/getter) ***********
    @property
    def type(self) -> str:
        return self.__type
    
    @type.setter
    def type(self, value: str) -> None:
        allowed_types = {"keeper", "striker", "defender", "midfielder"}
        self.__type = value.lower() if isinstance(value, str) and value.lower() in allowed_types else "unknown"

    # ********** static method get_goals_team ***********
    @staticmethod
    def get_goals_team() -> int:
        return Player.__number_goals_team

    # ********** property goals_player - (getter only) ***********
    @property
    def goals_player(self) -> int:
        return self.__goals_player

    def make_goal(self) -> None:
        self.__goals_player += 1
        Player.__number_goals_team += 1

    def __str__(self) -> str:
        return (f"Player: {self.firstname} {self.lastname} ({self.type}) "
                f"value: {self.value_player}/10, goals: {self.goals_player}, birthdate: {self.birthdate}")
    
    def __repr__(self) -> str:
        return (f"Player(lastname={self.lastname!r}, firstname={self.firstname!r}, "
                f"type={self.type!r}, value_player={self.value_player!r}, "
                f"goals_player={self.__goals_player!r}, birthdate={self.birthdate!r})")
