number=[1,2,4,6,3,7,8]
def missing_no():
    missing_no=0
    n = len(number)+1
    total= n* (n+1)//2
    missing = total - sum(number)
    return missing
print("missing number:",missing_no())