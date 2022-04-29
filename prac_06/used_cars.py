"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Volvo", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    print()
    print("Limo:")
# Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car(name="limo car", fuel=100)
# Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)
# Print the amount of fuel in the car.
    print("fuel =", limo.fuel)
# Attempt to drive the car 115 km using the drive method.
    distance_driven = limo.drive(115)
# Print the car's odometer reading.
    print(f"Actual distance Travelled = {distance_driven}")
    print("odo =", limo.odometer)
# Now add the __str__ method to the Car class in car.py.
    print(limo)


main()
