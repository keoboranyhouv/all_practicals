from taxi import Taxi
import random


class UnreliableCar(Taxi):

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        random_num = random.randint(0, 100)
        while random_num < self.reliability:
            distance_driven = super().drive(distance)
            self.current_fare_distance += distance_driven
            return distance_driven
