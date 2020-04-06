z=[1,2,3,5,8,4,7,9,1,4,12,5,6,5,2,1,0,8,1]

d={x:z.count(x) for x in z}     
print (d)                       
c=[]                            

for num in z:                   
    if num not in c:            
       c.append(num)             
print (c)                       


for j in c:                     
    for x in z:                 
        b=int(z.count(x))       
        if(j==x):               
            print (j,'-',b)     
            break               
