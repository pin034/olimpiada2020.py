a = int(input("Число секунд: \n"))
ch = a // 3600
a %= 3600
m = a // 60
a %= 60
print(ch, "ч.",m,"мин.",a,"c")
