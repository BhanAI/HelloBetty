class Animal:
    def __init__(self, name, babyName, move):
        self.name = name
        self.babyName = babyName
        self.move = move

    def printAnimal(self):
        print("The baby's name of {} is {} and it {}.".format(self.name, self.babyName, self.move))

a0 = Animal('dog', 'puppy', 'runs fast')
a0.printAnimal()
a1 = Animal('rabbit', 'kitten', 'hops')
a1.printAnimal()
a2 = Animal('pig', 'piglet', 'eats a lot')
a2 .printAnimal()