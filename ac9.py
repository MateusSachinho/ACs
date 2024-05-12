"""
Aluno: Mateus de Macedo Coelho Sachinho

Matrícula: 202403184672

AC9
EX1 - Distância
"""

def distancia():
    Km = int(input())
    tempo = Km*2
    print(tempo, "minutos")

#distancia()

"""
EX2 - Fatorial Simples
"""

def fatorial_simples(N):
    fatorial = 1
    for _ in range(1, N+1):
        fatorial *= _
    return fatorial

#print(fatorial_simples(int(input())))

"""
EX3 - Ida à Feira
"""
def feira():
    N = int(input())

    for _ in range(N):
        M = int(input())

        precos = {}

        for _ in range(M):
            fruta, preco = input().strip().split(' ')

            precos[fruta] = float(preco)

        P = int(input())

        resposta = 0.0
        for _ in range(P):
            fruta, quantidade = input().strip().split(' ')

            resposta += int(quantidade) * precos[fruta]

        print(f'R$ {resposta:.2f}')

#feira()

"""
EX4 - Identificando o Chá
"""

def cha():
    T = int(input())
    A,B,C,D,E = input().split(' ')
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    E = int(E)
    resposta = [A,B,C,D,E]
    print(resposta.count(T))

#cha()

"""
EX5 - Aviões de Papel
"""

def papel():
    C, P, F = map(int, input().split())
    total = C * F
    if total <= P:
        print('S')
    else:
        print('N')

#papel()

"""
EX6 - Tacógrafo
"""

def tacógrafo():
    N = int(input())
    total = 0
    for _ in range(N):
        tempo, vm = map(int, input().split())
        total += tempo * vm
    print(total)

#tacógrafo()

"""
EX7 - Busca na Internet
"""

def internet():
    t = int(input())
    print(4 * t)

#internet()

"""
EX8 - Sequência Secreta
"""

def sequencia():
    tamanho = int(input())
    lista = []
    total = 1

    for _ in range(tamanho):
        num = int(input())
        lista.append(num)
    anterior = lista[0]

    for item in lista:
        if anterior == item:
            continue
        else:
            total += 1
        anterior = item

    print(total)

#sequencia()

""""""

def main():
    distancia()
    print(fatorial_simples(int(input())))
    feira()
    cha()
    papel()
    tacógrafo()
    internet()

main()


