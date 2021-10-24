#  Python program for sum of the square of first N natural numbers

N = int(input("Enter value of N: "))

# calculating sum of square 
sumVal = 0
for i in range(1, N+1):
    sumVal += (i*i)

print("Sum of squares = ", sumVal)