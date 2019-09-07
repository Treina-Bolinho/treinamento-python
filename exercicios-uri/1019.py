# URI 1019
tempoSeg = int (input())

hora = int(tempoSeg // 3600)
min  = int(tempoSeg % 60 - (hora * 60))
seg = int(tempoSeg % 60)

print('{}:{}:{}'.format(hora, min, seg))