number=[1,1,2,2,2,3,3,1,1,1,1]
count = 1
maximum=1
for i in range(1,len(number)):
    if number[i]==number[i-1]:
        count+=1
    else:
        count=1
    if count > maximum:
        maximum = count
print("maximum consecution countt",maximum)
        
        
