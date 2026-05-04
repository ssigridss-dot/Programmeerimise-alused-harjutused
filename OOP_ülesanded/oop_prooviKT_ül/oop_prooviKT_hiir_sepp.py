class Mouse:
    """
    Represents a computer mouse.
    """

    count = 0

    def __init__(self, dpi, wireless):
        """
        Constructor.
        """
        self.dpi = dpi
        self.wireless = wireless
        Mouse.count += 1

    def click(self):
        """
        Simulates clicking.
        """
        return "Click"

    def info(self):
        """
        Mouse info.
        """
        return f"{self.dpi} DPI"


class GamingMouse(Mouse):
    """
    Inherited Mouse class.
    """

    def __init__(self, dpi=16000, wireless=True, rgb=True):
        """
        Default constructor.
        """
        super().__init__(dpi, wireless)
        self.rgb = rgb

    def mode(self):
        """
        RGB mode.
        """
        return "RGB enabled" if self.rgb else "No RGB"


if __name__ == "__main__":
    m = GamingMouse()
    print(m.click())
    print(m.info())
    print(m.mode())
    print(Mouse.count)