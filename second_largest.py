largest=0
second_largest=0
number=[12,35,1,10,34,35]
for num in number:
    if num>largest:
        second_largest=largest
        largest=num
    elif num > second_largest and num<largest:
     print("largest",largest)   
     print("second laegest",second_largest)