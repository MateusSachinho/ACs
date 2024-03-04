"""
Aluno: Mateus de Macedo Coleho Sachinho

Matrícula: 202403184672

AC1 - EX1: Equações de segundo grau

Pontos de observação
1 - Para começar, eu resolvi iniciar pelas variáveis a, b e c
2 - Aqui eu iria começar a botar as fórmulas para o PC resolver
3 - Percebi que eu não sabia como fazer raiz quadrada, então eu pesquisei que e descobri duas opções:
    Usar o comando import math para poder usar sqrt() que caucula a raiz quadrada ou elevar **0.5
"""
# Ponto de observação 1
def equação():
    print("-"*5,"Por favor, insira os valores", "-"*5)
    a = float(input("Insira o valor de A: "))
    b = float(input("Insira o valor de B: "))
    c = float(input("insura o valor de C: "))
    raiz1, raiz2 = mat(a, b , c)
    print("-"*15, "RESULTADO","-"*14)
    print("A primeira raiz é", raiz1)
    print("A segunda raiz é", raiz2)
    
    

# Ponto de observação 2
def mat(a, b, c):
    delta = (b**2 - 4*a*c)**0.5 # Ponto de observação 3
    raiz1 = (-b + delta)/2*a
    raiz2 = (-b - delta)/2*a
    return raiz1, raiz2
    


"""
EX2:anos bissextos

Pontos de observação
1 - Usei o int() pois sem ele, quando se for digitar o ano, o programa irá entender que é um string, mas
    o int() faz com que o ano seja entendido como inteiro, podendo assim realizar operações
2 - Para um número ser divisível por outro, tem que saber se o resto é igual á 0, logo temos que usar o % que 
    dará o resto da divisão
"""



def ano_bissexto():
    ano = int(input("Digite o ano: ")) # Ponto de observação 1
    bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0) # Ponto de observação 2
    print("O ano é bissexto?", bissexto)



def main():
    equação()
    print("-"*30)
    ano_bissexto()

main()