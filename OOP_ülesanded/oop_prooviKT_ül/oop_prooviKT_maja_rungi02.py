class House:
    """
    Represents a house.
    """

    count = 0

    def __init__(self, rooms, floors):
        """
        Constructor.
        """
        self.rooms = rooms
        self.floors = floors
        House.count += 1

    def live(self):
        """
        Living in house.
        """
        return "Living"

    def info(self):
        """
        House info.
        """
        return f"{self.rooms} rooms, {self.floors} floors"


class SmartHouse(House):
    """
    Inherited House class.
    """

    def __init__(self, rooms=3, floors=1, smart_system=True):
        """
        Default constructor.
        """
        super().__init__(rooms, floors)
        self.smart_system = smart_system

    def automation(self):
        """
        Smart system feature.
        """
        return "Automation ON" if self.smart_system else "Manual"


if __name__ == "__main__":
    h = SmartHouse()
    print(h.live())
    print(h.info())
    print(h.automation())
    print(House.count)