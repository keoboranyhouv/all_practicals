from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = 'q)uit, c)hoose taxi, d)rive'
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    current_taxi = None
    print("let's drive!")
    print(MENU)
    current_menu = input('>>> ').lower()
    while current_menu != "":
        if current_menu == 'c':
            print('Taxis available: ')
            display_taxi(taxis)
            chosen_taxi = int(input('Choose taxi: '))
            try:
                current_taxi = taxis[chosen_taxi]
            except IndexError:
                print('Invalid taxi choice')




    pass


def display_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')


if __name__ == '__main__':
    main()