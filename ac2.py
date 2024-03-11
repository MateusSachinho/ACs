"""
Aluno: Mateus de Macedo Coelho Sachinho

Matrícula: 202403184672

AC2 - EX1: revisite a AC1
Desenvolva duas funções em Python:
eq_seg_grau(a, b, c), que recebe três valores reais e retorna as raízes de uma equação de segundo grau no formato ax² + bx + c = 0,
supondo as raízes sempre reais

bissexto(ano), que recebe um valor inteiro e retorna um valor booleano, informando se o ano é bissexto ou não.


Pontos de observação
1 - Para resolver, basta usar o print() e trocar ax² + bx + c = 0 por (a,"*", raiz1,"² + ", b,"*", raiz1, "+", c, "= 0") para que
    apareça o resultado das raízes e os valores de a, b e c dados.

2 - Para resolver, basta fazer a mesma coisa, porém trocando raiz1 por raiz2

3 - Para resolver, foi necessário separar em duas partes, parecido com a função da equação de segundo grau, onde uma faz o cálculo e
    a outra "molda a resposta"


"""

def equação():
    print("-"*5,"Por favor, insira os valores", "-"*5)
    a = float(input("Insira o valor de A: "))
    b = float(input("Insira o valor de B: "))
    c = float(input("insura o valor de C: "))
    raiz1, raiz2 = mat(a, b , c)
    print("-"*15, "RESULTADO","-"*14)
    print("A primeira raiz é", raiz1)
    print("A segunda raiz é", raiz2)
    print(a,"*", raiz1,"² + ", b,"*", raiz1, "+", c, "= 0" ) # Ponto de observação 1
    print("ou")
    print(a,"*", raiz2,"² + ", b,"*", raiz2, "+", c, "= 0" ) # Ponto de observação 2
    print("ou")



def mat(a, b, c):
    delta = (b**2 - 4*a*c)**0.5 
    raiz1 = (-b + delta)/2*a
    raiz2 = (-b - delta)/2*a
    return raiz1, raiz2

#--------------------------------------------------------------------------------------------------

def ano_bissexto(ano): # Ponto de observação 3
    if ano % 400 == 0:
        return True
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    return False



def resposta(ano):
    if ano_bissexto(ano):
        print("O ano", ano, "é bissexto")
    else:
        print("O ano", ano, "não é bissexto")

"""
EX2: salário

Pontos de observação
1 - Para resolver, foi necessário montar duas contas, uma que calcula o irpf, e outra que calcula o salário
"""
def calcula_salario(): # Ponto de observação 1
    valor_hora = float(input("Insira o valor da hora: "))
    num_horas = float(input("Insira a quantidade de horas: "))
    irpf = (valor_hora * num_horas) * 0.275
    salário_líquido = (valor_hora * num_horas) - irpf
    print("Seu sálario é de ", salário_líquido)

#--------------------------------------------------------------------------------------------------

def main():
    equação()
    print("-"*30)
    ano = int(input("Digite o ano: "))
    resposta(ano)
    print("-"*30)
    calcula_salario()

main()
