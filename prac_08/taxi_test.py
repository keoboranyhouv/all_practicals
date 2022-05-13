from taxi import Taxi


def main():
    new_taxi = Taxi('Prius 1', 100)
    new_taxi.drive(40)
    print(new_taxi)
    print(f"Current fare: ${new_taxi.get_fare():.2f}")

    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi)
    print(f"Current fare: ${new_taxi.get_fare():.2f}")

main()
