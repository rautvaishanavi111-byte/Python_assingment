def palindrome(text,left,right):
    if left>=right:
        return True
    if text[left]!= text[right]:
        return False
    return palindrome(text,left+1,right -1)
text="racecar"
result=palindrome(text,0,len(text)-1)
print(result)