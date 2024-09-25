class Parent1:
    def method(self):
        print("Parent1 method")

class Parent2:
    def method(self):
        print("Parent2 method")

class Child(Parent1, Parent2):
    def method(self):
        super().method()
        Parent2.method(self)
        Parent2().method()
        print("Child method")

child = Child()
child.method()

