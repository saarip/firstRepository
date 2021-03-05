class Person:

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f"Name: {self.__name}, age: {self.__age}"

if __name__ == "__main__":
    somePerson = Person("Steve Yzerman", 55)
    print(somePerson.name)
    print(somePerson.age)
    print(somePerson)