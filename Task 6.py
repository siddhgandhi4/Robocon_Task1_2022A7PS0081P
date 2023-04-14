lis=[1,8,6,2,5,4,8,3,7]
li=[]
for i in range (0,len(lis)):
    for j in range (len(lis)-1,i,-1):
        if lis[i]>lis[j]:
            a=lis[j]*(j-i)
            li.append(a)
        else:
            a=lis[i]*(j-i)
            li.append(a)

li.sort()
print(li[-1])


        
