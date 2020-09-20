a = int(input())
b = int(input())
i = 2
while i > 0:
    for x in range (1,i):
        e = a * x + 1
        i = i + 1
        if e % b +1 == b:
            print(e)
            i = 0
