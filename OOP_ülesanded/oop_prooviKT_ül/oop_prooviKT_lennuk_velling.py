class Airplane:
    """
    Represents an airplane.
    """

    count = 0

    def __init__(self, model, capacity):
        """
        Constructor.
        """
        self.model = model
        self.capacity = capacity
        Airplane.count += 1

    def fly(self):
        """
        Simulates flying.
        """
        return "Flying"

    def info(self):
        """
        Airplane info.
        """
        return f"{self.model}, {self.capacity}"


class PassengerPlane(Airplane):
    """
    Inherited airplane.
    """

    def __init__(self, model="Boeing", capacity=200, airline="VellingAir"):
        """
        Default constructor.
        """
        super().__init__(model, capacity)
        self.airline = airline

    def airline_info(self):
        """
        Returns airline.
        """
        return f"Airline: {self.airline}"


if __name__ == "__main__":
    a = PassengerPlane()
    print(a.fly())
    print(a.info())
    print(a.airline_info())
    print(Airplane.count)