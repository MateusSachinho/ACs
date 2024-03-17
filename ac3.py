"""
Aluno: Mateus de Macedo Coelho Sachinho

Matrícula: 202403184672

AC3 - EX1: triângulos

Pontos de observação
1 - Para saber se um triângulo existe, é preciso saber sobre a condição de existência de um triângulo, que diz
    "se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo"
    logo, para saber se o triângulo existe ou não, é preciso botar as equações A + B < C, A + C < B, B + C < A no começo da função.
2 - Para um triângulo ser equilátero é necessário que todos os lados sejam iguais 
3 - Para um triângulo ser isósceles é necessário 2 lados sejam iguais 
4 - Para um triângulo ser escaleno é necessário que todos os lados sejam diferentes
"""

def identificar_triângulos(A, B, C):

    if A + B < C: # Ponto de observação 1
        print("Não é um triângulo")
        return
    
    if A + C < B:
        print("Não é um triângulo")
        return
    
    if B + C < A:
        print("Não é um triângulo")
        return
    
    if A == B == C: # Ponto de observação 2
        print("O triângulo é equilátero")
        return

    if A == B: # Ponto de observação 3
        print("O triângulo é isósceles")
        return
        
    if A == C:
        print("O triângulo é isósceles")
        return
    
    if B == C:
        print("O triângulo é isósceles")
        return
    
    if A != B != C: # Ponto de observação 4
        print("O triângulo é escaleno")
        return
    
    else:
        return

"""
AC3 - EX2: dia da semana

Pontos de observação
1 - Para resolver, é preciso de uma função para ler o valor inteiro e reornar o dia da semana e outra função para ter o print da 1° função
"""

def dia_da_semana(dia): # Ponto de observação 1
    if dia == 1:
        return "Domingo"

    if dia == 2:
        return "Segunda-feira"

    if dia == 3:
        return "Terça-feira"

    if dia == 4:
        return "Quarta-feira"

    if dia == 5:
        return "Quinta-feira"

    if dia == 6:
        return "Sexta-feira"

    if dia == 7:
        return "Sábado"
    
    else:
        return ""

def testa_dia_da_semana():
    print(dia_da_semana(2))  
    print(dia_da_semana(6))  
    print(dia_da_semana(7))  
    print(dia_da_semana(9))

"""
AC3 - EX3: calculadora simples

Pontos de observação
1 - Função feita para: Coletar os números, a operação que será feita e mostrar o resultado da conta
2 - Função feita para: Realizar as operações e retornar o resultado

"""

def calculadora(): # Ponto de observação 1

    num1 = float(input("Informe um número: "))
    num2 = float(input("Informe outro número: "))
    operação = input("Informe a operação (soma, subtração, multiplicação, divisão): ")

    resultado = operacao(num1, num2, operação)
    print("Resultado:", resultado)



def operacao(num1, num2, operação): # Ponto de observação 2
        if operação == "soma":
            return num1 + num2
        
        if operação == "subtração":
            return num1 - num2
        
        if operação == "multiplicação":
            return num1 * num2
        
        if operação == "divisão":
            return num1 / num2
        
        else:
            return "Operação inválida"



#----------------------------------------------------------------------------------------------------------------------



def main():
    identificar_triângulos(4 , 4, 4)

    identificar_triângulos(2 , 4, 4)

    identificar_triângulos(3 , 4, 5)
    
    identificar_triângulos(1 , 1, 4)

    print("-"*30)

    testa_dia_da_semana()

    print("-"*30)

    calculadora()
main()