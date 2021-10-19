def ispalindromString(strng):
    new_strng=strng
    if strng[::-1]==new_strng:
        return "Yes"
    else:
        return "No"

# Driver main code
if __name__ == '__main__':
    strn=input("Enter a value whome you want check it is palindrome or not")
    res=ispalindromString(strn)
    if res == 'Yes':
        print("Yes your string",strn,'is palindrome')
    else :
        print("Yes your string", strn, 'is not palindrome')