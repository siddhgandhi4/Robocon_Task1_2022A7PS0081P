li=input("Enter a sring: ")
lis=li.replace(' ','')
if len(lis)%2!=0:
    print("false")
else:
    for i in range (0,len(lis),2):
        z=1
        if lis[i]=="{"and lis[i+1]=="}":
            continue
        elif lis[i]=="("and lis[i+1]==")":
            continue
        elif lis[i]=="["and lis[i+1]=="]":
            continue
        else:
            z=0
            break
if z==0:
    print("False")
else:
    print("True")
    
            
    
        
        
        
    
    
   
    
    


           
   

        
            
        
    
