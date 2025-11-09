import random

def Calculate():
    start = (input("Ready? y/n"))
    if start == "y":
        asmd = random.randint(1, 4)     

        if asmd == 1:
            print("Addition")
            a1 = random.randint(0, 1000000)
            a2 = random.randint(0, 1000000)
            a3 = (a1 + a2)
            print(a1)
            print("+")
            print(a2)
            print("= %d!" % a3)
            Calculate()

        if asmd == 2:
            print("Subtraction")
            s1 = random.randint(0, 1000000)
            s2 = random.randint(0, 1000000)
            s3 = (s1 - s2)
            print(s1)
            print("-")
            print(s2)
            print("= %d!" % s3)
            Calculate()

        if asmd == 3:
            print("Multiplication")
            m1 = random.randint(0, 1000000)
            m2 = random.randint(0, 1000000)
            m3 = (m1 * m2)
            print(m1)
            print("X")
            print(m2)
            print("= %d!" % m3)
            Calculate()

        if asmd == 4:
            print("Division")
            d1 = random.randint(1, 1000000)
            d2 = random.randint(1, 1000000)
            d3 = (d1 * d2)
            print(d1)
            print("/")
            print(d2)
            print("= %d!" % d3)
            Calculate()    

Calculate()
