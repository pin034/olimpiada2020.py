d = 0
print("начальное время")
CH, M, S = map(int, input().split())
print("конечное время")
chk, mk, sk = map(int, input().split())
razn = (chk * 3600 + mk * 60 + sk) - (CH * 3600 + M * 60 + S)
if razn > d:
    cho = razn // 3600
    mo = (razn % 3600) // 60
    so = razn % 60 
else:
    razn = razn + 24 * 3600
    cho = razn // 3600
    mo = (razn % 3600) // 60
    so = razn % 60 
print(cho," ", mo," ", so)
