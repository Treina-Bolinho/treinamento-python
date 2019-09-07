# URI - 1013

li = input().split(" ")
a, b, c = li

m2 = (int(a) + int(b) + abs(int(a) - int(b ))) / 2
m2 = (int(c) + m2     + abs(int(c) - m2))      / 2

print ('{} eh o maior'.format(int(m2)))