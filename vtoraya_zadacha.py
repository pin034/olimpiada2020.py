print("начальное время")
CH, M, S = map(int, input().split())
print("конечное время")
chk, mk, sk = map(int, input().split())
razn = (chk * 3600 + mk * 60 + sk) - (CH * 3600 + M * 60 + S)
cho = razn // 3600
mo = (razn % 3600) // 60
so = razn % 60 
print(cho," ", mo," ", so)