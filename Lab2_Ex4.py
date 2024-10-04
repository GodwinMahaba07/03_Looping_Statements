def generate_inverted_triangle(n):
    if n > 0:
        print("*" * n)
        generate_inverted_triangle(n - 1)

n = int(input("Enter the height of the triangle: "))
generate_inverted_triangle(n)

