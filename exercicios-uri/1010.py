# URI - 1010

l1 = input().split(" ")
l2 = input().split(" ")

a0, b0, c0 = l1
a1, b1, c1 = l2

x = (b0 * c0) + (b1 * c1)
print ('VALOR A PAGAR: R$ {:.2}'.format(x))