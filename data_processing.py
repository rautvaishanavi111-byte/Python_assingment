number=[-2,1,2,3,4,6,-8]
def process_numbers(numbers):
    total=0
    count=0
    largest=None
    for num in numbers:
      if num >= 0 and num%2==0:
        square = num * num
        total = total + square
        count = count + 1
        if largest is None or square > largest:
           largest = square
    print("total",total)
    print("count",count) 
    print("largest squared value:",largest )
process_numbers(number)