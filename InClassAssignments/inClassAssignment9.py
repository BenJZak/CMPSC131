class Zookeeper:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__animals = {}
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getAge(self):
        return self.__age
    def setAge(self, age):
        self.__age = age
    def getAnimals(self):
        return self.__animals
    def addAnimals(self, animals):
        self.__animals.update(animals)


zookeeper1 = Zookeeper("Ben", 20)
zookeeper1.addAnimals({"Shawn": "Sheep", "Buns": "Bunny", "Squiggly": "Squirrel", "Harry": "Hippo", "Donald": "Duck"})
zookeeper2 = Zookeeper("Zoozoo", 89)
zookeeper2.addAnimals({"Arnie": "Ape", "Caroline": "Cow", "Bobby": "Baboon", "Presley": "Panther", "Peter": "Pig"})

print(f"{zookeeper1.getName()}'s age: {zookeeper1.getAge()}. He is taking care of the following animals:")
for key, value in zookeeper1.getAnimals().items():
    print(f"{key} the {value}")

print(f"{zookeeper2.getName()}'s age: {zookeeper2.getAge()}. They are taking care of the following animals:")
for key, value, in zookeeper2.getAnimals().items():
    print(f"{key} the {value}")