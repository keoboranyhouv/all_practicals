from taxi import Taxi


class SilverServiceTaxi(Taxi):

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness
        self.current_fare_distance = 0

    def get_fare(self):
        """Return the price for the taxi trip."""
        return (self.price_per_km * self.current_fare_distance) + self.flagfall

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km " \
               f"plus flagfall of ${self.flagfall} "

