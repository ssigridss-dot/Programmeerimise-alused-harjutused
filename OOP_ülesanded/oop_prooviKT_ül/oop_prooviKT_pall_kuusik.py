class Ball:
    """
    Represents a ball.
    """

    count = 0

    def __init__(self, sport, size):
        """
        Constructor.
        """
        self.sport = sport
        self.size = size
        Ball.count += 1

    def bounce(self):
        """
        Ball bounce.
        """
        return "Bounce"

    def info(self):
        """
        Ball info.
        """
        return f"{self.sport}, size {self.size}"


class SportsBall(Ball):
    """
    Inherited Ball class.
    """

    def __init__(self, sport="football", size=5, pressure="normal"):
        """
        Default constructor.
        """
        super().__init__(sport, size)
        self.pressure = pressure

    def check_pressure(self):
        """
        Pressure check.
        """
        return f"Pressure: {self.pressure}"


if __name__ == "__main__":
    b = SportsBall()
    print(b.bounce())
    print(b.info())
    print(b.check_pressure())
    print(Ball.count)