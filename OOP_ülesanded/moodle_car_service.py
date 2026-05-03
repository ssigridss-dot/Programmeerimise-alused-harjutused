"""Car service."""


class Car:
    """Represent car model."""

    def __init__(self, color: str, make: str, engine_size: int):
        """
        Car class constructor.

        :param color: car color
        :param make: car make
        :param engine_size: car engine size
        """
        self.color = color
        self.make = make
        self.engine_size = engine_size


class Service:
    """Represent car service model."""

    def __init__(self, name: str, max_car_num: int):
        """
        Service class constructor.

        Car service should also have a database to keep and track all cars standing in queue for repair.
        :param name: service name
        :param max_car_num: max car number service can take for repair at one time
        """
        self.name = name
        self.max_car_num = max_car_num
        self.queue = []

    def can_add_to_service_queue(self, car: Car) -> bool:
        """
        Check if it possible to add car to service queue.

        Car can be added if:
        1. after adding new car, total car number in service does not exceed max_car_number (allowed car number in service)
        2. there is no car with the same color and make present in this service (yes, this world works this way).

        If car can be added, return True. Otherwise return False.
        """
        # kontroll 1: kas auto mahub järjekorda
        if len(self.queue) >= self.max_car_num:
            return False

        # kontroll 2: sama color + make ei tohi juba olemas olla
        for c in self.queue:
            if c.color == car.color and c.make == car.make:
                return False
        return True

    def add_car_to_service_queue(self, car: Car):
        """
        Add car to service if it is possible.

        The function does not return anything.
        """
        if self.can_add_to_service_queue(car):
            self.queue.append(car)

    def get_service_cars(self) -> list:
        """Get all cars in service."""
        return self.queue

    def repair(self) -> Car:
        """
        Repair car in service queue.

        Normally, the first car in queue is repaired.
        However, if there is a car in queue which color + make characters length is exactly 13 ->
        this car is chosen and is repaired (might be multiple suitable cars -> choose any).
        After the repair, car is no longer in queue (is removed).
        :return: chosen and repaired car
        """
        if not self.queue:
            return None

        # otsi erijuht (color + make pikkus == 13)
        for i, car in enumerate(self.queue):
            if len(car.color + car.make) == 13:
                return self.queue.pop(i)

        # muidu esimene järjekorras
        return self.queue.pop(0)

    def get_the_car_with_the_biggest_engine(self) -> list:
        """
        Return a list of cars (car) with the biggest engine size.

        :return: car (cars) with the biggest engine size
        """
        if not self.queue:
            return []

        # lühem variant 1.
        # max_engine = max(car.engine_size for car in self.queue)
        # return [car for car in self.queue if car.engine_size == max_engine]

        # pikem variant 2.
        # leia suurim engine_size
        max_engine = None
        for car in self.queue:
            if max_engine is None or car.engine_size > max_engine:
                max_engine = car.engine_size

        # kogu kõik autod, millel on see suurim engine_size
        result = []
        for car in self.queue:
            if car.engine_size == max_engine:
                result.append(car)
        return result


if __name__ == '__main__':
    service = Service("MyService", 3)

    car1 = Car("red", "Toyota", 1800)
    car2 = Car("blue", "BMW", 2500)
    car3 = Car("black", "Audi", 2500)

    service.add_car_to_service_queue(car1)
    service.add_car_to_service_queue(car2)
    service.add_car_to_service_queue(car3)

    print("Cars in service:")
    for car in service.get_service_cars():
        print(car.color, car.make, car.engine_size)

    biggest = service.get_the_car_with_the_biggest_engine()
    print("\nBiggest engine cars:")
    for car in biggest:
        print(car.color, car.make, car.engine_size)

    repaired = service.repair()
    print("\nRepaired car:", repaired.color, repaired.make)