class CoatRack:
    """
    Represents a coat rack.
    """

    count = 0

    def __init__(self, hooks, material):
        """
        Constructor.
        """
        self.hooks = hooks
        self.material = material
        CoatRack.count += 1

    def hang(self):
        """
        Simulates hanging coats.
        """
        return "Coats hung"

    def info(self):
        """
        Returns rack info.
        """
        return f"{self.hooks} hooks, {self.material}"


class WallCoatRack(CoatRack):
    """
    Inherited coat rack.
    """

    def __init__(self, hooks=5, material="wood", wall_type="brick"):
        """
        Default constructor.
        """
        super().__init__(hooks, material)
        self.wall_type = wall_type

    def wall_info(self):
        """
        Returns wall type info.
        """
        return f"Wall type: {self.wall_type}"


if __name__ == "__main__":
    c = WallCoatRack()
    print(c.hang())
    print(c.info())
    print(c.wall_info())
    print(CoatRack.count)