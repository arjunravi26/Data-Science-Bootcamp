class Work:
    def __init__(self,work_hour) -> None:
        self.work_hour = work_hour
        print("working hour setted")
    def do(self):
        print(f"Person Can Work for {self.work_hour}")


class Person(Work):
    def __init__(self, name, age, place,work_hour) -> None:
        super().__init__(work_hour)
        self.name = name
        self._age = age
        self.__place = place

    def print(self):
        return f"Name is {self.name} and age is {self._age} and place is {self.__place}"

    def change_name(self, name):
        print(f"Old name {self.name} changing to {name}...")
        self.name = name
        print("Successful")
        return self.name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def change_place(self, place):
        pass

    def __repr__(self) -> str:
        return f"Name is {self.name} and age is {self._age} and place is {self.__place}. Class name is {Person.__name__} and class is {Person}"

    def __str__(self):
        return f"Name is {self.name} and age is {self._age} and place is {self.__place}"


person = Person("Arjun", 21, "Kottayam",12)
print(person)
print(person.print())
print(person.change_name("Arjun Ravi"))
print(person._age)
# name mangling (to make this place variable private, python add _ClassName before the actual variable)
print(person._Person__place)
print(person.__repr__())
print(person.age)
person.age = 22
print(person.age)
print(person.do())
