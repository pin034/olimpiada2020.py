a,b,c,d = map(int,input("Введите четыре целых числа: \n").split(" "))
if a > b and c and d:
    print("Наибольшее число",a)
elif b > c and d and a:
    print("Наибольшее число",b)
elif c > d and b and a:
    print("Наибольшее число",c)
else:
    print("Наибольшее число",d)
