# code for armstrong number
def isArmstrong(num): # declaring a function to check given number is armstrong or not
    x=str(num) # storing num into x as string
    y=len(x) # strong the length of string x
    new_val=0 # declaring a value to take sum of the nth power of digit of given number (n=number of digit in given number)
    while num!=0: # calculating new_val
        z=num%10
        new_val=new_val+z**y
        num=num//10
    if new_val==int(x): #comparing new_val to the original number
        return "Yes"
    else :
        return "No"
# Driver code
if __name__ == '__main__':
    val=int(input("Enter a number"))
    res=isArmstrong(val) # calling function isArmstrong()
    if res=="Yes": # checking the result
        print("The given number ",val," is an Armstrong Number")
    else:
        print("The given number ", val, " is not an Armstrong Number")