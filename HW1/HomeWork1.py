__author__ = 'Mohan Kumar Velaga'

count = 0

def findthenumber(num1,num2) :
    global count
    count = count +1
    gussednum = (num1+num2)//2
    result = input("is it "+ str(gussednum) +"? (yes/no)")
    while True :
        if (result == 'yes' or result == 'no') :
            break
        print("Please enter a valide input")
        result = input("is it "+ str(gussednum) +"? (yes/no)")
    if(result == "yes") :
        return gussednum
    else :
        result1 = input("Is the number larger than " + str(gussednum) + "? (yes/no)")
        while True :
            if (result1 == 'yes' or result1 == 'no') :
                break
            print("Please enter a valide input")
            result1 = input("Is the number larger than " + str(gussednum) + "? (yes/no)")
        if(result1 == "yes") : return findthenumber(gussednum+1,num2)
        else                 : return findthenumber(num1,gussednum-1)

# Main Program
name = input("Hi What is your name?")
print("Hello "+ name +"! Let's play a game!")
print("Think of random number from 1 to 100, and I'll try to guess it!")
while True :
    findthenumber(1,100)
    print("Yeey! I got it in " + str(count) + " tries!")
    count = 0
    c = input("Do you want to play more?")
    if (c == "no") : break
print("Bye-bye")