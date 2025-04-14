# ------------------------------What is a class in python?
#A blueprint for creating an object

# ------------------------------What is an object in python?
#A specific instance of a class

# ------------------------------How do python classes relate to python objects?
#they are the way that objects are built, like a base structure to base the object off of

# ------------------------------How do you create a python class?
class pokemon:
    def __init__(self, name, species, hp, attack):
        self.name = name
        self.species = species
        self.hp = hp
        self.attack = attack
    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nHp: {self.hp}\nAttack: {self.attack}"
    def fight(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            if self.hp > 0:
                opponent.hp -= self.attack
            print(f"{self.name}'s hp is {self.hp}")
            print(f"{opponent.name}'s hp is {opponent.hp}")
            if opponent.hp > 0:
                self.hp -= opponent.attack
            print(f"{self.name}'s hp is {self.hp}")
            print(f"{opponent.name}'s hp is {opponent.hp}")

bob = pokemon("Mr.Bob", "Charizard", 300, 280)
bobby = pokemon("Mr.Bobby", "Arcanine", 400, 110)
boberto = pokemon("Mr.Boberto", "Pikachu", 360, 115)
print(bob)

# ------------------------------What are methods?
#A function that is specific to a class

# ------------------------------How do you create a python object?
#name_of_new_object = class_name(parameters)

# ------------------------------How to you call a method for an object?
#name of object, put a period, put the name of the method, then put parameters in it

# ------------------------------Why do we use python classes?
#because it organizes information better, it is more convenient, simplifies later code