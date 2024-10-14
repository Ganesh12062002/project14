class college:
    def __init__(self,id,name):
        self.id=id
        self.name=name

class student(college):
    def __init__(self,id,name,city):
        super().__init__(id,name)
        self.city=city

obj =student(101,"om","pune")
print(obj.id)
print(obj.name)
print(obj.city)
print(obj.city)
