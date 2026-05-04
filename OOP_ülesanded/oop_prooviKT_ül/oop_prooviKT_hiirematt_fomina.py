class Mousepad:
    """
    Represents a mousepad.
    """

    count = 0

    def __init__(self, size, color):
        """
        Constructor.
        """
        self.size = size
        self.color = color
        Mousepad.count += 1

    def use(self):
        """
        Simulates usage.
        """
        return "Using mousepad"

    def info(self):
        """
        Returns info.
        """
        return f"{self.size}, {self.color}"


class GamingMousepad(Mousepad):
    """
    Inherited mousepad.
    """

    def __init__(self, size="L", color="black", rgb=True):
        """
        Default constructor.
        """
        super().__init__(size, color)
        self.rgb = rgb

    def lighting(self):
        """
        RGB lighting feature.
        """
        return "RGB on" if self.rgb else "No RGB"


if __name__ == "__main__":
    m = GamingMousepad()
    print(m.use())
    print(m.info())
    print(m.lighting())
    print(Mousepad.count)