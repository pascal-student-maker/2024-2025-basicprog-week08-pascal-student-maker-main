from model.Birthdate import Birthdate

def test_birthdates_basics():
    # Create a valid Birthdate instance
    date1 = Birthdate(25, 9, 1977)
    print(date1)

    try:
        date1.day = 32  # Try to set an invalid day (should raise ValueError)
    except ValueError as e:
        print(f"Error: {e}")
    print(date1)

    # Create another Birthdate instance
    date2 = Birthdate(25, 9, 1977)
    
    if date1 == date2:
        print("Date1 and Date2 are equal!")

    # Create a third Birthdate instance with a different date
    date3 = Birthdate(25, 11, 2023)
    
    if date2 != date3:
        print("Date2 and Date3 are not equal!")

    # Print a list of Birthdate objects
    list_dates = [date1, date2, date3]
    print("\nList of Birthdates:")
    for bd in list_dates:
        print(bd)

# Run the test function
test_birthdates_basics()
