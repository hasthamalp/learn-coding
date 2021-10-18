def multiplePatternSystem(a):
    if a.upper()=='A':
        pyramid()
    elif a.upper()=='B':
        reversePyramid()
    elif a.upper()=='C':
        rightStartPyramid()
    elif a.upper()=='D':
        leftStartPyramid()
    elif a.upper()=='E':
        halfPyramid()
    elif a.upper()=='F':
        leftHalfPyramid()
    elif a.upper()=='G':
        downwardHalfPyramid()
    elif a.upper()=='H':
        dimondShaped()
    else:
        linearStar()
#Wapp to print * Pattern
#***
#***
#***
def linearStar():
    n= int(input("enter a number"))
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()
#Wapp to print * pattern
#*
#**
#***
def halfPyramid():
    n= int(input("enter a number"))
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()
#Wapp to print * pattern
#***
#**
#*
def downwardHalfPyramid():
    n= int(input("enter a number"))
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print()
#Wapp to print * pattern
#  *
# **
#***
def leftHalfPyramid():
    n= int(input("enter a number"))
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        print()
#Wapp to print * pattern
#*****
# ***
#  *
def reversePyramid():
    n=int(input("enter a number"))
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range(n-i):
            print("*",end="")
        for k in range(n-i-1):
            print("*",end="")
        print()
#Wapp to print a pattern
# *
#***
def pyramid():
    n=int(input("enter a number"))
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print()
# Wapp to print rightStartPyramid
# *
# **
# ***
# **
# *
def rightStartPyramid():
    n=int(input("enter a number"))
    for i in range(0, n):
        for j in range(0, i + 1):
            print("*", end="")
        print()
    for i in range(n, 0 , -1):
        for j in range(0, i + 1):
           print("*", end="")
        print()
    print("*")
# Wapp to print leftStartPyramid
#    *
#   **
#  ***
# ****
#  ***
#   **
#    *
def leftStartPyramid():
    n=int(input("enter a number"))
    k = 2 * n - 2
    for i in range(0, n - 1):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print()
    k = -1
    for i in range(n - 1, -1, -1):
        for j in range(k, -1, -1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print()
# Wapp diamondShappedPyramid
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
def dimondShaped():
     n=int(input("enter a number"))
     k = 2 * n - 2
     for i in range(0, n):
         for j in range(0, k):
             print(end=" ")
         k = k - 1
         for j in range(0, i + 1):
             print("* ", end="")
         print()
     k = n - 2
     for i in range(n, -1, -1):
         for j in range(k, 0, -1):
             print(end=" ")
         k = k + 1
         for j in range(0, i + 1):
             print("* ", end="")
         print()

#Driver Main Code
if __name__ == '__main__':
    print("Welcome to the Star System")
    print("Here is the list of Star system")
    print("A : pyramid  , B : reversePyramid  , C : rightStartPyramid  , D : leftStartPyramid   , E : halfPyramid    , F : leftHalfPyramid   ,G : downwardHalfPyramid    , H: diamondShapped  , other : linear")
    choice=input("Select one among any of the choices [A,B,C,D,E,F,G,H]")
    multiplePatternSystem(choice)


