f = int(input())
e = int(input())
e = e+1
a = 0
b = 0
for x in range(f,e):
    if x % 2 == 0:
        a = a + x
    else:
        b = b + x
a = a - b
print (a)
