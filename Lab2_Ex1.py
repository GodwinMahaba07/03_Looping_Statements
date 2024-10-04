
#Godwin Anton M. Mahaba
#BSCpe 2-2
#DSA: Lab 2 - Exercise 1


def power(base, exponent):

    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

base = 2
exponent = 7
result = power(base, exponent)
print(f"The result of {base} raised to the power of {exponent} is: {result}")
