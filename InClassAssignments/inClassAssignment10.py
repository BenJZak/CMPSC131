class Animal:
    def __init__(self, name):
        self.__name = name
    def speak(self, sound):
        print(f"{self.__name} makes a sound. {self.__name} says {sound}!")
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed
    def get_breed(self):
        return self.__breed

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed
    def get_breed(self):
        return self.__breed

dog = Dog("Rex", "Pitbull")
print(f"{dog.get_name()} is a {dog.get_breed()}")
dog.speak("Bark")
cat = Cat("Whiskers", "Tabby")
print(f"{cat.get_name()} is a {cat.get_breed()}")
cat.speak("Meow")
