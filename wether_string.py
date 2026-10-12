first="listen"
second="silent"
if len(first)!= len(second):
    print(False)
else:
    count={}
    for ch in first:
        if ch in count:
            count[ch]+=1
        else:
            count[ch]=1
    for ch in second:
        if ch in count:
            count[ch]-=1
        else:
            count[ch]= -1
    result = True
    for value in count.values():
        if value !=0:
            result = False
            break
print(result)