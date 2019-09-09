# URI 1035
li = [int(i) for i in input().split()]
a, b, c, d = li
  
if (a%2 == 0) and (c>0 and d>0) and (b>c and d>a) and (c+b > a+b):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")