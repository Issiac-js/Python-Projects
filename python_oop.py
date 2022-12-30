




# parent class

class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "sequence A"
    origin = "Unknown"
    carbon_based = True


    
     # def __init__ for the class cahllenge.
    def __init__(self, name="Unknown", species='Unknown', legs = None, arms = None, dna = "sequence A", origin = "Unknown"):
        self.name = name
        self.species = species
        self.legs = legs
        self.arms = arms
        self.dna = dna
        self.origin = origin
    
    def information(self):
        msg = "\nName:{}\nSpecies:{}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name, self.species, self.legs, self.arms, self.dna, self.origin, self.carbon_based)
        return msg
     







# child class instance
class Human(Organism):
    name = "Macguyver"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

# another child class instance
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = 'Earth'

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
        return msg


# another child class instance
class Bacterium(Organism):
    name = "X"
    species = "Bactieria"
    legs = 0
    arms = 0
    dna = "Squence C"
    origin = "Mars"

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two seprate organisms!"
        return msg





if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication)



    new_orangism = Organism("Test", "test one")
    print(new_orangism.information())


















