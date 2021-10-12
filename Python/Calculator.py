# Program for a Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

print("Select operation:")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")

while True:
    
    choice = input("Enter choice(a/b/c/d): ")

    
    if choice in ('a', 'b', 'c', 'd'):
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if choice == 'a':
            print(n1, "+", n2, "=", add(n1, n2))

        elif choice == 'b':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif choice == 'c':
            print(n1, "*", n2, "=", multiply(n1, n2))

        elif choice == 'd':
            print(n1, "/", n2, "=", divide(n1, n2))
        break
    else:
        print("Invalid Input")
