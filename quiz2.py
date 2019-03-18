
class Animal:
    def __init__(self,name, species):
        self.species = species
        self.name = name
        
    
    def make_noise(self):
        print(self)
tiger = Animal("Roar!")
dog = Animal("Bark!")
cow = Animal("Moo!")

class Zoo:
    def __init__(self, animals):
        animals = []
    
    def add(self,animal):
        Zoo.animals.append(Animal(name))
    
    def show_animals(self):
        For animal in Zoo(animals):
            print(animal,Animal.make_noise(animal))

#sorry this is crap.  totally studied sql stuff, db stuff over the classes

