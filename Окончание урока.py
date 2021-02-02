a = int(input("Введите номер урока: \n"))
v = 500
for i in range(a):
    v += 55
ch = v //60
m = v %60
print(ch,"-", m)
