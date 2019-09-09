# URI 1036 - sem math e com com função
#-----------------------------------------------------
def main():
    li = [float(i) for i in input().split(" ")]
    a, b, c = li

    x1, x2 = baskara(a, b, c)

    if x1 and x2:
        print ("Impossivel calcular") 
    else:
        print('R1 = {:.5f}'.format(x1))
        print('R2 = {:.5f}'.format(x2))
#-----------------------------------------------------
def baskara (a, b, c):
    delta  = b**2 - 4*a*c
    if a!=0:
        if delta > 0:
            return deltaMaior(a, b, delta)

        if delta ==  0:
            return deltaIgual(a, b)
    
    return True, True
#-----------------------------------------------------
def deltaMaior(a, b, delta):
    x1 = (-b + delta ** (1/2)) / (2*a)
    x2 = (-b - delta ** (1/2)) / (2*a)
    return x1, x2
#-----------------------------------------------------
def deltaIgual(a, b):
    x = -b / (2*a) 
    return x, x
#-----------------------------------------------------
if __name__ == '__main__':
    main()