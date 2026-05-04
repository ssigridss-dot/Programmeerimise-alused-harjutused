class Bed:
    """
    Represents a bed.
    """

    count = 0

    def __init__(self, size, material):
        """
        Constructor.
        """
        self.size = size
        self.material = material
        Bed.count += 1

    def sleep(self):
        """
        Simulates sleeping.
        """
        return "Sleeping"

    def info(self):
        """
        Bed info.
        """
        return f"{self.size}, {self.material}"


class SmartBed(Bed):
    """
    Inherited Bed class.
    """

    def __init__(self, size="Queen", material="wood", smart=True):
        """
        Default constructor.
        """
        super().__init__(size, material)
        self.smart = smart

    def features(self):
        """
        Smart bed features.
        """
        return "Smart features enabled" if self.smart else "Basic bed"


if __name__ == "__main__":
    b = SmartBed()
    print(b.sleep())
    print(b.info())
    print(b.features())
    print(Bed.count)