from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = 'q)uit, c)hoose taxi, d)rive'


def main():
    total_taxi_bill = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("let's drive!")
    print(MENU)
    current_menu = input('>>> ').lower()

    while current_menu != "q":
        if current_menu == 'c':
            print('Taxis available: ')
            display_taxi(taxis)
            chosen_taxi = int(input('Choose taxi: '))
            try:
                current_taxi = taxis[chosen_taxi]
            except IndexError:
                print('Invalid taxi choice')

        elif current_menu == 'd':
            if current_taxi is not None:
                current_taxi.start_fare()
                distance = float(input('Drive how far? '))
                current_taxi.drive(distance)
                trip_fare = current_taxi.get_fare()
                print(f'Your {current_taxi.name} trip cost you ${trip_fare:.2f}')

                total_taxi_bill += trip_fare
            else:
                print('You need to choose a taxi before you can drive')



def display_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')


if __name__ == '__main__':
    main()
