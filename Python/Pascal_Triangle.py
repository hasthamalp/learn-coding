n = int(input("Enter the number: "))  
l = []   

for i in range(n):  
  l.append([])  
  l[i].append(1)  

  for j in range(1, i):  
    l[i].append(l[i - 1][j - 1] + l[i - 1][j])  

  if(n != 0):  
    l[i].append(1) 

for i in range(n):  
  print(" " * (n - i), end = " ", sep = " ")  

  for j in range(0, i + 1):  
    print('{0:6}'.format(l[i][j]), end = " ", sep = " ")  

  print()  