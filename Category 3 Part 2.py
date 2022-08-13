T = int(input("Enter the number of desired tests"))
R = range(1, 1000)
for x in range(T):
    if T in R:
        for x in range(T):
            X = int(input("Enter the first height"))
            Y = int(input("Enter the second height"))
            if X == Y:
                print("Heights have to be different")
            if X < 100 or X > 200 or Y < 100 or Y > 200:
                print("Heights cannot be less than 100cm or more than 200cm")
            if X > Y:
                print("a")
            else:
                print("b")

    else :
        print("Number of tests cannot exceed 1000")
