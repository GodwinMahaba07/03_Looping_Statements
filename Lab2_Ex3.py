
#Godwin Anton M. Mahaba
#BSCpe 2-2
#DSA: Lab 2 - Exercise 3



def generate_hollow_square():

    n = int(input("Enter the side length of the square: "))

    border = "x" * n
    print(border)

    for i in range(n - 2):
        interior = "x" + " " * (n - 2) + "x"
        print(interior)

    print(border)

generate_hollow_square()
