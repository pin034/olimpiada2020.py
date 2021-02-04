a = int(input("Возраст Антона: "))
b = int(input("Возраст Бориса: "))
c = int(input("Возраст Виктора: "))
if a == b and c:
    print("У всех один возраст.")
elif a == b and a > c:
    print("Антон и Борис старше Виктора.")
elif a == c and a > b:
    print("Антон и Виктор старше Бориса.")
elif c == b and c > a:
    print("Борис и Виктор старше Антона.")
elif b > a and b > c:
    print("Борис старше всех.")
elif c > a and c > b:
    print("Виктор старше всех.")
else:
    print("Антон старше всех.")
