from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def add(self,a,b):
        pass

class Derivate(Base):
    def add(self,a,b):
        return a + b
d = Derivate()
print(d.add(4,3))
