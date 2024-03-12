"""
programação estruturada
2024.1
12/03/2024

Mateus Sachinho
202403184672

AC5
"""
import random

# Gera um valor aleatório entre 2 e 8
"""
def aventureiro():
    vida = 100
    atk = random.randint(10, 20)
    defe = random.randint(1, 5)
    print("aventureiro:","vida", vida, "atk",atk, "defesa", defe)

def monstro():
    vida_m = random.randint(60, 80)
    atk_m = random.randint(20, 30)
    defe_m = 0
    print("monstro:", "vida", vida_m, "atk",atk_m, "defesa", defe_m)
"""
def main():

    vida = 100
    atk = random.randint(10, 20)
    defe = random.randint(1, 5)
    print("aventureiro:","vida", vida, "atk",atk, "defesa", defe)

    vida_m = random.randint(60, 80)
    atk_m = random.randint(20, 30)
    print("monstro:", "vida", vida_m, "atk",atk_m)
    
  
    rodada = 1

    while vida > 0 and vida_m > 0:
        print("rodada", rodada)
        rodada += 1 
        vida -= atk_m + defe 
        vida_m -= atk

        if vida <= 0:
            print("Você perdeu")
            break

        if vida_m <= 0:
            print("Você ganhou")
            break

        
        print("aventureiro:","vida", vida, "atk",atk, "defesa", defe)
        print("monstro:", "vida", vida_m, "atk",atk_m)
    


main()

"""
def main():
    aventureiro()
    monstro()

main()
"""






