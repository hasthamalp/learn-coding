str=input("string:")
s=int(input("shift:"))
f=""
b=""
for i in str:
    f+=chr(ord(i)+s)
    b+=chr(ord(i)-s)

print("forward shift:",f)
print("backward shift:",b)
