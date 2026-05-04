class House:
    """House class."""

    def __init__(self, rooms, floors, address):
        """House constructor."""
        self.rooms = rooms
        self.floors = floors
        self.address = address

    def print_info(self):
        """Print info of the given house."""
        print(f"Address: {self.address}")
        print(f"Rooms: {self.rooms}")
        print(f"Floors: {self.floors}")

    def renovate(self, new_rooms):
        """Calculate new rooms after renovation."""
        if new_rooms <= 0:
            raise ValueError("Number of rooms must be greater than 0.")
        print(f"Renovating house at {self.address}...")
        self.rooms = new_rooms
        print("Renovation completed.")

    def evaluate(self):
        """Evaluate price of the house."""
        # Simple base price calculation
        if self.rooms <= 0 or self.floors <= 0:
            raise ValueError("Invalid house data for valuation.")
        price = (self.rooms * 10000) + (self.floors * 5000)
        return price


class Villa(House):
    """Villa class."""

    def __init__(self, rooms, floors, address, luxury_factor):
        """Villa class constructor."""

        super().__init__(rooms, floors, address)
        self.luxury_factor = luxury_factor

    # Polymorphism: overridden method
    def evaluate(self):
        """Evaluate price of the given house."""

        base_price = super().evaluate()
        return base_price * self.luxury_factor

    def print_info(self):
        """Calculate luxory factor of the house."""

        super().print_info()
        print(f"Luxury factor: {self.luxury_factor}")


if __name__ == '__main__':
    try:
        house = House(3, 1, "Main Street 10")
        villa = Villa(5, 2, "Ocean Drive 99", 2.5)

        # Print info
        house.print_info()
        print("House value:", house.evaluate())
        print()

        villa.print_info()
        print("Villa value:", villa.evaluate())
        print()

        # Renovation
        house.renovate(4)
        print("New house value:", house.evaluate())
        print()

        # Polymorphism demo
        buildings = [house, villa]
        for b in buildings:
            print(f"{type(b).__name__} value:", b.evaluate())

        # Error example (uncomment to test)
        # house.renovate(-2)

    except ValueError as e:
        print("Error:", e)