a=int(input("Enter the area"))
li=[]
for b in range (1,a//2+1):
    lis=[]
    if a%b == 0:
        c=a/b
        lis.append(c)
        lis.append(b)
        li.append(lis)
d = (li[0][0]-li[0][1])
for r in range(len(li)):
    if abs(li[r][0]-li[r][1]) < d:
        d = abs(li[r][0]-li[r][1])
        an = li[r]
print(an)
