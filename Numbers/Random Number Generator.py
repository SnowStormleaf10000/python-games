import random

def randomnumber():
    rando = int(input("How much?"))
    print(random.randint(0, rando))
    randomnumber()

randomnumber()
