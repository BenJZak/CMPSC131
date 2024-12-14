
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__miles = 0
        self.__year = year

    #getters
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_miles(self):
        return self.__miles

    #setters
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_miles(self, miles):
        if miles > self.__miles:
            self.__miles = miles
            return True
        return False

class Person:
    def __init__(self, first_name, last_name, age, car=None):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__car = car
    
    #getters
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age

    def get_car(self):
        return self.__car

    #setters
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_age(self, age):
        self.__age = age

    def set_car(self, car):
        if self.__age >= 16:
            self.__car = car
    
def main():
    person = Person("Harrison", "Zakielarz", 15)
    car = Car("Honda", "Accord", 2003)
    car.set_miles(200000)
    person.set_car(car)
    print("Car for person (age < 16):", person.get_car())
    person.set_age(17)

    person.set_car(car)

    while True:
        try:
            new_miles = int(input("Enter new miles for the car: "))
            if car.set_miles(new_miles):
                break
            else:
                print("Miles must be greater than the current miles. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    print("First Name:", person.get_first_name())
    print("Last Name:", person.get_last_name())
    print("Age:", person.get_age())
    if person.get_car():
        print("Car Make:", person.get_car().get_make())
        print("Car Model:", person.get_car().get_model())
        print("Car Year:", person.get_car().get_year())
        print("Car Miles:", person.get_car().get_miles())
    else:
        print("Car: None")

if __name__ == "__main__":
    main()