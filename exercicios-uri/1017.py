# URI 1017

consumoLitro = 12
tempo = int (input ())
velocidadeMedia = int (input ())

distancia = tempo * velocidadeMedia
consumoViagem = distancia / consumoLitro

print ('{:.3f}'.format(consumoViagem))
