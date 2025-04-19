n =int(input("enter star value:"))  

for i in range (n):
    for k in range(0,n-i*1):
        print(" ", end=" ")
    for j in range (0,i):
        print(' * ', end= " ") 
    print(" ")  



for i in range(n):
    for k in range(0,i):
        print(" ", end=" ")
    for j in range(n-i*1):
        print(" * ", end=" ")
    print() 
