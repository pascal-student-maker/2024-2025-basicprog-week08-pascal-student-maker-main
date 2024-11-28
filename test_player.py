from model.Player import Player
from model.Birthdate import Birthdate

def test_ex4():
    player1 = Player("Thibault", "Courtous", "keeper", 8, Birthdate(11, 5, 1992))
    player2 = Player("Vincent", "Kompany", "striker", 8, Birthdate(10, 4, 1986))
    player3 = Player("Axel", "Witsel", "striker")  # No birthdate --> default value (1/1/2024)

    print("\nThe birthdates of the players are:")
    for item in [player1, player2, player3]:
        print(f"{item} -> Birthdate: {item.birthdate}")

test_ex4()
