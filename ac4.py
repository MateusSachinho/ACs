"""
Aluno: Mateus de Macedo Coelho Sachinho | 202403184672

"""
def ler_nome_usuario():
    return input("Informe o seu nome: ")



def ler_notas():
    ap1 = float(input("Informe a nota da ap1: "))
    ap2 = float(input("Informe a nota da ap2: "))
    asub = float(input("Informe a nota da as: "))
    ac = float(input("Informe a nota da ac: "))
    return ap1, ap2, asub, ac



def validar_notas(ap1, ap2, asub, ac):
    if ac > 10:
        return False
    if ac <= 0:
        return False
    if asub > 10:
        return False
    if asub <= 0:
        return False
    if ap2 > 10:
        return False
    if ap2 <= 0:
        return False
    if ap1 > 10:
        return False
    if ap1 <= 0:
       return False 
    
    return True
    


def duas_maiores_notas(ap1, ap2, asub):
    if asub > ap2:
        return ap1, asub
    if asub > ap1:
        return asub, ap2

    return ap1, ap2



def calcular_media(n1, n2, ac):
    media = (n1 + n2) * 0.4 + ac * 0.2
    return media



def informar_aprovacao(media):
    if media < 7:
        print("Sua média foi", media,"Você foi reprovado")
    if media >= 7:
        print("Sua média foi", media, "Você foi aprovado")



def main():
    nome = ler_nome_usuario()
    if nome:
        ap1, ap2, asub, ac = ler_notas() # Ler notas do usuário
        if validar_notas(ap1, ap2, asub, ac): # verificar se as notas são vazias
        # se forem válidas:
             n1, n2 = duas_maiores_notas(ap1, ap2, asub) # definir as duas maiores notas, entre ap1, ap2 e as
             media = calcular_media(n1, n2, ac) # calcular a média
             informar_aprovacao(media) # dizer se o aluno está aprovado ou não        


main()