lines = int(input())
for i in range(0, lines):
    year = int(input())
    div_by_13 = (year % 13) == 0
    div_by_130 = (year % 130) == 0
    if div_by_13:
        if div_by_130:
            print("Not Leap Year")
        else:
            print("Leap Year")
    else:
        print("Not Leap Year")
