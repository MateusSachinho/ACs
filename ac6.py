"""
Aluno: Mateus de Macedo Coelho Sachinho

Matrícula: 202403184672

-AC6- 
EX1: Hello World!
"""

print("Hello World!")

"""
EX2: Extremamente Básico
"""
A = float(input())   
B = float(input())

X = A + B

print("X =", X)

"""
EX3: Cálculo Simples
"""

código_1, quantidade_1, valor_unitário_1 = map(float,input().split())
pagar = quantidade_1*valor_unitário_1

código_2, quantidade_2, valor_unitário_2 = map(float,input().split())
pagar2 = quantidade_2*valor_unitário_2

total = pagar + pagar2

print("VALOR A PAGAR: R${:.2f}".format(total))

"""
EX4: O Maior
"""

n1, n2, n3 = map(float, input().split())
n4 = (n1 + n2 + abs(n1 - n2))/2
o_maior = (n4 + n3 + abs(n4 - n3))/2
print("{:.0f} eh o maior".format(o_maior))

"""
EX5: Distância Entre Dois Pontos
"""

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

Distância = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5

print("{:.4f}".format(Distância))
