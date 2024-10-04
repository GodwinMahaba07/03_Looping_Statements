
#Godwin Anton M. Mahaba
#BSCpe 2-2
#DSA: Lab 2 - Exercise 2


def cube_elements():
   
    size = int(input("Input the size of the array: "))

    elements = list(map(int, input("Input the elements separated by space: ").split()))

    for element in elements:
        cube = element ** 3
        print(cube)

cube_elements()
