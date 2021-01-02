# https://towardsdatascience.com/imagining-the-world-in-terms-of-classes-and-objects-fe04833a788c

# Class for animals
class Animal:
    category = "pets"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        print("Name of this animal is: ", self.name)

    def printage(self):
        print("Age of this animal is: ", self.age)

    def move(self):
        print("Running")


# Instantiate Animal objects
dog = Animal("Titu", 5)
cat = Animal("Sarah", 6)

# Call Instance Methods
dog.printname()
dog.printage()
dog.move()

cat.printname()
cat.printage()
cat.move()