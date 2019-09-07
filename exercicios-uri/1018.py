# URI 1018
valor = int (input ())

print('{}'.format(valor))
if (valor >= 100):
    notas100 = valor // 100
    valor -= notas100 * 100
else: notas100 = 0 
    
if (valor >= 50):
    notas50 = valor // 50
    valor -= notas50 * 50
else: notas50 = 0 

if (valor >= 20):
    notas20 = valor // 20
    valor -= notas20 * 20  
else: notas20 = 0 

if (valor >= 10):
    notas10 = valor // 10
    valor -= notas10 * 10  
else: notas10 = 0 

if (valor >= 5):
    notas5 = valor // 5
    valor -= notas5 * 5  
else: notas5 = 0 
    
if (valor >= 2):
    notas2 = valor // 2
    valor -= notas2 * 2  
else: notas2 = 0 

notas1 = valor

print ('{} nota(s) de R$ 100,00\n'.format(notas100) +
       '{} nota(s) de R$ 50,00\n'.format(notas50) +
       '{} nota(s) de R$ 20,00\n'.format(notas20) +
       '{} nota(s) de R$ 10,00\n'.format(notas10) +
       '{} nota(s) de R$ 5,00\n'.format(notas5) +
       '{} nota(s) de R$ 2,00\n'.format(notas2) +
       '{} nota(s) de R$ 1,00'.format(notas1))