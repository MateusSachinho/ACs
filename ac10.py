"""
Mateus de Macedo Coelho Sachinho
202403184672

AC10 - EX1 - Camisetas
"""
#Não consegui resolver
def ler():

    todas = []
    while True:
        N = int(input().strip())
        if N == 0:
            break

        turma = []

        for _ in range(N):
            nome = input().strip()
            cor, tamanho = input().strip().split()
            turma.append({'cor': cor, 'tamanho': tamanho, 'nome': nome})

        todas.append(turma)
    
    return todas

def ordenar(todas):

    tamanho_ordem = {'P': 3, 'M': 2, 'G': 1} 

    for turma in todas:
        turma.sort(key=lambda x: (x['cor'], tamanho_ordem.get(x['tamanho']), x['nome']))
    return todas

def resultados(todas):

    for i, turma in enumerate(todas):
        if i > 0:
            print("") 

       
        for camiseta in sorted(turma, key=lambda x: x['nome']):
            print(f"{camiseta['cor']} {camiseta['tamanho']} {camiseta['nome']}")

def camisetas():
    todas = ler()
    todas = ordenar(todas)
    resultados(todas)

#camisetas()

"""
EX2 - Espécies de Madeira
"""


def calcular(arvores):
    ordenadas = dict(sorted(arvores.items()))
    total = sum(ordenadas.values())

    for especie, quantidade in ordenadas.items():
        porcentagem = (quantidade / total) * 100
        print(f"{especie} {porcentagem:.4f}")


def especies_de_madeira():
    testes = int(input(""))
    input()

    for _ in range(testes):
        quantidade = 0
        arvores = {}

        while True:
            try:
                especie = input()
                
                if especie == "":
                    break
                
                if especie in arvores:
                    arvores[especie] += 1
                else:
                    arvores[especie] = 1

                quantidade += 1

            except EOFError:
                break

        calcular(arvores)

        arvores = {}
        quantidade = 0

        if _ < testes - 1:
            print()

#especies_de_madeira()


"""
EX3 - Escada do DINF
"""
def escada_do_dinf():
    while True:
        try:
            degrau = int(input())
            h, c, l = input().split()
            h = float(h)
            c = float(c)
            l = float(l)

            hipo = ((c**2) + (h**2)) ** 0.5
            hipo *= (l / 100 * degrau) / 100
            print('%.4f' % hipo)

        except EOFError:
            break

#escada_do_dinf()


""""""
def main():
    camisetas()
    especies_de_madeira()
    escada_do_dinf()

main()









