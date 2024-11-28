# model/HotelRepository.py

from model.Hotelguest import Hotelguest

class HotelRepository:
    
    @staticmethod
    def read_hotel_guests(file_path: str) -> list:
        """
        Reads the guest data from a file and returns a list of Hotelguest objects.
        
        :param file_path: Path to the file containing guest data.
        :return: List of Hotelguest objects.
        """
        guests = []
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    # Assuming the file has data in the format: lastname, firstname, balance
                    data = line.strip().split(',')
                    if len(data) == 3:
                        lastname, firstname, balance = data
                        balance = float(balance)  # Convert balance to a float
                        guest = Hotelguest(lastname.strip(), firstname.strip(), balance)
                        guests.append(guest)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except Exception as e:
            print(f"Error: {str(e)}")
        
        return guests
