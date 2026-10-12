def analyze_marks(*args):
    if len(args)==0:
        print("no mark provided")
        return
    total = 0
    highest = args[0]
    passing = 0
    for mark in args:
        total = total + mark
        if mark>highest:
            highest = mark
        if mark >=40:
            passing = passing + 1
    average=total/len(args)
    print("total:",total)
    print("Average:",average)
    print("highest:",highest)
    print("passing count:",passing)
analyze_marks(75,86,95,94,76)    