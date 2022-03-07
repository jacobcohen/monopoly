from location import Location   

class Player:

    def __init__(self, location: Location, name: str):
        self.current_location = location
        self.name = name
        print(f"Created player: '{name}'!")