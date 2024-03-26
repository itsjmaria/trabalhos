def soma (a,b):
    return a+b
    
def quadrado (a):
    return a**2

def hipotenusa (cat1, cat2):
    return soma (quadrado(cat1),quadrado(cat2)) ** (1/2)

def simples (cor):
    if cor == 'rosa' :
        return 'escolheu certo'

numeros= [1,2,3,4,5]

print("===comecei o loop while===")
contador = 0
while contador < 10:
    print (contador, end=' ')
    contador += 1
    
    def desenhar_triangulo(num_linhas):
    for linha in range(1, num_linhas + 1):
        print('*' * linha)
