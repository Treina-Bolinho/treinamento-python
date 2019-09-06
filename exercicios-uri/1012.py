# URI - 1012

pi =  3.14159
li = input().split(" ")
a, b, c = li

areaTriangulo = float(a) * float(c) / 2
areaCirculo   = pi * float(c) ** 2
areaTrapezio  = (float(a) + float(b)) * float (c) / 2
areaQuadrado  = float(b) ** 2
areaRetangulo = float(a) * float(b) 

print('TRIANGULO: {:.3f}\n'.format(areaTriangulo) +
      'CIRCULO: {:.3f}\n'.format(areaCirculo)     + 
      'TRAPEZIO: {:.3f}\n'.format(areaTrapezio)   +
      'QUADRADO: {:.3f}\n'.format(areaQuadrado)   +
      'RETANGULO: {:.3f}'.format(areaRetangulo))