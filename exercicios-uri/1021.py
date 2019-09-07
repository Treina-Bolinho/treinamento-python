# URI 1021

valor = float (input())

c100 = valor // 100
resto = valor - c100 * 100
c50  = resto // 50
resto -= c50 * 50
c20  = resto // 20
resto -= c20 * 20
c10  = resto // 10
resto -= c10 * 10
c5   = resto // 5
resto -= c5 * 5
c2   = resto // 2
resto -= c2 * 2
#-----------------------------------
resto *=  100
m100 = int(resto // 100)
resto -= m100 * 100
m50  = resto // 50
resto -= m50 * 50
m25  = resto // 25
resto -= m25 * 20
m10  = resto // 10
resto -= m10 * 10
m5   = resto // 5
resto -= m5 * 5
m1   = resto
#-----------------------------------
print('NOTAS')
print ('{} nota(s) de R$ 100.00\n'.format(int(c100)) +
       '{} nota(s) de R$ 50.00\n'.format(int(c50)) +
       '{} nota(s) de R$ 20.00\n'.format(int(c20)) +
       '{} nota(s) de R$ 10.00\n'.format(int(c10)) +
       '{} nota(s) de R$ 5.00\n'.format(int(c5)) +
       '{} nota(s) de R$ 2.00\n'.format(int(c2)))

print('MOEDAS')

print ('{} moeda(s) de R$ 1.00\n'.format(int(m100)) +
       '{} moeda(s) de R$ 0.50\n'.format(int(m50)) +
       '{} moeda(s) de R$ 0.25\n'.format(int(m25)) +
       '{} moeda(s) de R$ 0.10\n'.format(int(m10)) +
       '{} moeda(s) de R$ 0.05\n'.format(int(m5)) +
       '{} moeda(s) de R$ 0.01\n'.format(int(m1)
       