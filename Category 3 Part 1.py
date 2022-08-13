T = int(input("Enter the number of test cases"))
i = 0
if T < 1 or T > 1000:
    print("Invalid input")
while T > i:
    if T < 1 or T > 1000:
        break
    X = int(input("Enter the number of rupees that need to be paid"))
    if X < 1 or X > 1000:
        print("Invalid input")
        break
    i += 1
    num_str = repr(X)
    last_digit_str = num_str[-1]
    last_digit = int(last_digit_str)
    print("The minimum number of coins required is", last_digit, "to pay", X, "rupess")