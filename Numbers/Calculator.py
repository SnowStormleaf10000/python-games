def Calculate():
    asmd = int(input("Please choose an operation, Addition(1), Subtraction(2), Multiplication(3), Division(4), or Cubing(5)?"))
    if asmd == 1:
        a1 = int(input("Please pick your first number"))
        a2 = int(input("Please pick your second number"))
        a3 = (a1 + a2)
        print("Your answer is: %d!" % a3)
        Calculate()

    if asmd == 2:
        s1 = int(input("Please pick your first number"))
        s2 = int(input("Please pick your second number"))
        s3 = (s1 - s2)
        print("Your answer is: %d!" % s3)
        Calculate()

    if asmd == 3:
        m1 = int(input("Please pick your first number"))
        m2 = int(input("Please pick your second number"))
        m3 = (m1 * m2)
        print("Your answer is: %d!" % m3)
        Calculate()

    if asmd == 4:
        d1 = int(input("Please pick your first number"))
        d2 = int(input("Please pick your second number"))
        if d2 == 0:
            print("Nuh-uh!")
            Calculate()
        else:
            print("Your answer is:")
            print(d1 / d2)
            Calculate()

    if asmd == 5:
        sq1 = int(input("Please pick your number to be cubed."))
        sq2 = (sq1 * sq1 * sq1)
        print("Your answer is: %d!" % sq2)
        Calculate()

Calculate()
