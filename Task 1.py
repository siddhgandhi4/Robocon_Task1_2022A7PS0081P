def fac(n):
    fact=1
    if n==0:
        return 1
    for i in range (1,n+1):
        fact=fact*i
    return fact


def nCr(n,r):
    b=fac(n)/(fac(r)*fac(n-r))
    return b
    
    


while True:
    row=int(input("The number of rows: "))
    if row in range (1,31):
        break
    else:
        print("Value of row not in range of 1 to 30")
        
numbers=[1]
triangle=[]
triangle.append(numbers)
for i in range (1,row):
    numbers=[]
    for j in range (0,i+1):
        numbers.append(int(nCr(i,j)))
        j=j+1
    triangle.append(numbers)
    i=i+1
print(triangle)
        
        
    

