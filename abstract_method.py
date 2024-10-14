from abc import ABC,abstractmethod

class person(ABC):
    @abstractmethod
    def add(self):pass

    def sub(self):pass

class B(person):
    def add(self):
        print("in add impementation")
obj=B()
obj.add()
obj.sub()