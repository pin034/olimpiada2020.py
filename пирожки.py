a,d = map(int,input("Стоимость пирожка: \n").split(" "))
c = int(input ("Сколько пирожков: \n"))
kop = d * c
d = kop % 100
a = (a * c)+(kop // 100)
print("К оплате:",a,"руб.",d,"коп.")
