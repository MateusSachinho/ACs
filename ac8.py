"""
Mateus de Macedo Coelho Sachinho
202403184672

AC8

EX-1-Figurinhas
"""

def mdc(a, b):

    while b:
        a, b = b, a % b
    return a


def pilhas():
    T = int(input())

    for _ in range(T):

        F1, F2 = map(int, input().split())
        print(mdc(F1, F2))


#pilhas()


"""
EX-2-Dama
"""

def movimentos(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0  
    elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return 1  
    else:
        return 2  

def dama():
    while True:
        x1, y1, x2, y2 = map(int, input().split())

        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break  
            
        print(movimentos(x1, y1, x2, y2))


#dama()


"""
EX-3-Soma de Fatoriais
"""
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def soma_dos_fatoriais():
    while True:
        try:
            M, N = map(int, input().split())
           
            print(calcular_fatorial(M) + calcular_fatorial(N))
        except EOFError:
            break

#soma_dos_fatoriais()

"""
EX-4-Blobs
"""

def calcular_dias_comida(C):
    dias = 0
    while C > 1:  
        C /= 2  
        dias += 1 
    return dias

def blobs():
    T = int(input())
    for _ in range(T):
        C = float(input())
        print(calcular_dias_comida(C), "dias")


#blobs()


"""
EX-5-Frequência de Números
"""
def Frequência():

    N = int(input())
    numeros = [int(input()) for _ in range(N)]
    diferentes = set(numeros)

    for valor in sorted(diferentes):
        frequência = numeros.count(valor)
        print(f"{valor} aparece {frequência} vez(es)")


#Frequência()


"""
EX-6-Primo Rápido
"""

def teste_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primo_rápido():
    N = int(input())

    for _ in range(N):
        X = int(input())
        if teste_primo(X):
            print("Prime")
        else:
            print("Not Prime")


#primo_rápido()


"""
EX-7-Cara ou Coroa
"""

def cara_ou_coroa():
    while True:
        T = int(input())
        if T == 0:
            break
        
        resultados = list(map(int, input().split()))
        vitória = {'Maria': 0, 'João': 0}
        
        for _ in resultados:
            if _ == 0:
                vitória['Maria'] += 1
            else:
                vitória['João'] += 1
        
        print("Mary won {} times and John won {} times".format(vitória['Maria'], vitória['João']))


#cara_ou_coroa()


"""
EX-8-Funções
"""

def função_r(x, y):
    return (3*x)**2 + y**2

def função_b(x, y):
    return 2*(x**2) + (5*y)**2

def função_c(x, y):
    return -100*x + y**3

def funções():
    N = int(input())

    for _ in range(N):
        x, y = map(int, input().split())
        
        rafael = função_r(x, y)
        beto = função_b(x, y)
        carlos = função_c(x, y)
        
        if rafael > beto and rafael > carlos:
            print("Rafael ganhou")
        elif beto > rafael and beto > carlos:
            print("Beto ganhou")
        else:
            print("Carlos ganhou")


#funções()


"""
"""
def main():

    pilhas()
    dama()
    soma_dos_fatoriais()
    blobs()
    Frequência()
    primo_rápido()
    cara_ou_coroa()
    funções()

#main()
