class Car:
    def __init__(self, year, make):
        self.__year_model = year
        self.__make = make
        self.__consumption = 26
        self.__tank = 0

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

        # methods

    def drive(self, distance):
        self.__tank -= distance / self.__consumption

    def fill_up(self, amount):
        self.__tank += amount

    def get_mpg(self):
        return self.__consumption

    def get_gas(self):
        return self.__tank


def main():
    my_car = Car('2020', 'Ferrari Roma')

    print('Tank: ', my_car.get_gas())
    my_car.fill_up(20)
    print('fill 20 liters')
    print('Tank: ', my_car.get_gas())
    print('Drive 200km')
    my_car.drive(200)
    print('Tank: ', my_car.get_gas())

    # Call the main function


main()
