# URI - 1010

la = input().split()
lb = input().split()

a = int(la[1]) * float(la[2])
b = int(lb[1]) * float(lb[2])

print ('VALOR A PAGAR: R$ {:.2f}'.format(a + b))