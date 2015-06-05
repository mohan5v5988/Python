from random import randint

class Animal :
    all_animals = []
    def __init__(self,name,q1,q2,q3):
        self.name = name
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
    @staticmethod
    def getAnimalAtIndex(index): return Animal.all_animals[index]
    def getName(self) : return self.name
    def guess_who_am_i(self) :
        print(self.q1)
        a = input("Who am I?: ")
        if (a == self.name) : return True
        print("Nope, try again!")
        print(self.q2)
        a = input("Who am I?: ")
        if (a == self.name) : return True
        print("Nope, try again!")
        print(self.q3)
        a = input("Who am I?: ")
        if (a == self.name) : return True
        print("Nope, try again!")
        return False

lion = Animal("lion","I am the biggest cat","I live in groups","I am the King of the jungle")
elephant = Animal("elephant","I am the largest land-living mammal in the world","I have exceptional memory","I have Trunk")
tiger = Animal("tiger","I am the biggest cat","I come in black and white or orange and black","I an the national animal of INDIA")
bat  = Animal("bat","I use echo-location","I can fly","I see well in dark")
dog  = Animal("dog","I live with human","I am the animal used for sniffing","I don't like cat's")
cat  = Animal("cat","I live with human","I acted in tom and jerry","My favourite food is rat")
dolphin  = Animal("dolphin","I have exceptional memory","I live in water","I play with human")
Animal.all_animals.append(lion)
Animal.all_animals.append(elephant)
Animal.all_animals.append(tiger)
Animal.all_animals.append(bat)
Animal.all_animals.append(dog)
Animal.all_animals.append(cat)
Animal.all_animals.append(dolphin)
i = "yes"
print("I will give you 3 hints, guess what animal I am")
while (i != "no"):
    animal = Animal.getAnimalAtIndex(randint(0,6))
    if (animal.guess_who_am_i()) :
        print("You got it! I am ",animal.getName())
    else:
        print("I'm out of hints! The answer is: ",animal.getName())
    i = input("Do you want to play (yes/no): ")