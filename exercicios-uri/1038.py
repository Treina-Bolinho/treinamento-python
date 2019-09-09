# URI 1038
#-----------------------------------------------------
def main():
    
    cod, qtd = map(int, input().split()) 
    valor = codValor(cod)
    total = qtd * valor
    print('Total: R$ {:.2f}'.format(total))
#-----------------------------------------------------
def codValor (cod):
    switcher = {
        1: 4.00,
        2: 4.50,
        3: 5.00,
        4: 2.00,
        5: 1.50,
    }
    return switcher.get(cod, "Nao encontradado")   
#-----------------------------------------------------
if __name__ == '__main__':
    main()