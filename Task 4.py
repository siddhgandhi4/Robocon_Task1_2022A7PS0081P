i=0
j=0
lis=input("Enter the commands: ")
for k in lis:
    if k=="U":
        j+=1
    elif k=="D":
        j-=1
    elif k=="R":
        i+=1
    else:
        i-=1
if j==0 and i==0:
    print("True")
else:
    print("False")
    
    

