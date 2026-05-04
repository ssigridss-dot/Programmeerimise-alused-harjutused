class Mug:
    """
    Represents a mug (cup).
    """

    count = 0

    def __init__(self, volume, material):
        """
        Constructor for Mug.
        """
        self.volume = volume
        self.material = material
        Mug.count += 1

    def drink(self):
        """
        Simulates drinking from mug.
        """
        return "Drinking from mug"

    def info(self):
        """
        Returns mug information.
        """
        return f"{self.volume}ml, {self.material}"


class CoffeeMug(Mug):
    """
    Inherited Mug class.
    """

    def __init__(self, volume=300, material="ceramic", insulated=True):
        """
        Default constructor.
        """
        super().__init__(volume, material)
        self.insulated = insulated

    def temperature_control(self):
        """
        Checks insulation.
        """
        return "Keeps hot" if self.insulated else "No insulation"


if __name__ == "__main__":
    m = CoffeeMug()
    print(m.drink())
    print(m.info())
    print(m.temperature_control())
    print(Mug.count)