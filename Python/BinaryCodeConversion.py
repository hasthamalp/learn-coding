# Code for conversion of decimal number to binary
# Using Recursion method
def DecimalBinaryCodeConversion(dec_num):
    if dec_num >= 1:
        DecimalBinaryCodeConversion(dec_num// 2)
    print(dec_num % 2, end='')


# Main Code
if __name__ == '__main__':
    # Entering decimal value
    dec_value = int(input("Enter a decimal value"))
    print("Your Binary code of ",dec_value," is ")
    # Calling DecimalBinaryCodeConversion function
    DecimalBinaryCodeConversion(dec_value)