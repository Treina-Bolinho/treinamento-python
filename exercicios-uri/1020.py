# URI 1020
nDias = int (input())

ano = nDias // 365
mes = (nDias % 365) / 30
dia = (mes - int(mes)) * 30

print('{} ano(s)\n'.format(ano) +
      '{} mes(es)\n'.format(int(mes)) +
      '{} dia(s)'.format(int(dia))) 