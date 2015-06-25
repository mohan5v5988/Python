from random import randint


class Numbers :
    def __init__(self):
        self.a = randint(0,500)
        self.b = randint(1,500)
    def output(self):
        return self.a//self.b
i = "yes"

while (i != "no") :
    print("INTEGER DIVISIONS")
    obj = Numbers()
    try:
        r = int(input(str(obj.a) + "/" + str(obj.b) + " = "))
        if ( r == obj.output() ) :
            print("CORRECT!")
        else:
            print("INCORRECT!")
    except (ValueError) :
        print("Please enter Integers Only!")
    i = input("Do you want to play (yes/no): ")