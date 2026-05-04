class Keyboard:
    """
    Represents a keyboard.
    """

    count = 0

    def __init__(self, layout, switches):
        """
        Constructor.
        """
        self.layout = layout
        self.switches = switches
        Keyboard.count += 1

    def type(self):
        """
        Simulates typing.
        """
        return "Typing..."

    def info(self):
        """
        Keyboard info.
        """
        return f"{self.layout}, {self.switches}"


class GamingKeyboard(Keyboard):
    """
    Inherited Keyboard class.
    """

    def __init__(self, layout="US", switches="mechanical", rgb=True):
        """
        Default constructor.
        """
        super().__init__(layout, switches)
        self.rgb = rgb

    def lighting(self):
        """
        RGB lighting.
        """
        return "RGB ON" if self.rgb else "RGB OFF"


if __name__ == "__main__":
    k = GamingKeyboard()
    print(k.type())
    print(k.info())
    print(k.lighting())
    print(Keyboard.count)