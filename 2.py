

n= int(input("Fibonaci series:"))
if n<0:
    print('grater then n value:')
else:
    print("fibo series:", end=" ") 
    
    
for i in range (n):
    print(first , end=" ")
    temp=first
    first=secount
    secount=temp+secount
    

n = 10
a, b = 0, 1

print('Fibonaci series:',end=" ")
for _ in range(n):
        
    print(a, end=" ")
    a, b = b, a + b

print('.')   



 


