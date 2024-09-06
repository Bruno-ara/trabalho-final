from time import sleep
import os
import pandas as pd
import random


def limpar():
    os.system('cls')


def lin():
    print('-' * 30)


tabela = pd.read_csv("tabela_jogadores.csv", sep=",")
num = list(tabela.index)

def sorteio_jogador():
    a = random.choice(num)
    nome_jogador = tabela.loc[a, "Nome"]
    gols = tabela.loc[a, "Gols"]
    return a, nome_jogador, gols


def roleta_sorteio(a):
    lin()
    print("META: 5000 gols")
    lin()
    sleep(3.5)
    for i in range(a + 1):
        nome_jogador = tabela.loc[i, "Nome"]
        print(nome_jogador)  
        sleep(0.6)
        
        limpar()
    lin()


def menu_escolha(gols):
    lin()
    print("""
1 - Gols na carreira
2 - Gols duplicados
3 - Gols triplicados
----META: 5000 gols----
""")
    
    while True:
        opcao = int(input("Escolha uma opção: "))
        lin()
        if opcao == 1:
            return gols
        elif opcao == 2:
            return gols * 2
        elif opcao == 3:
            return gols * 3
        else:
            print("Opção inválida. Tente novamente.")


def jogar():
    estatisticas = {}
    s = 0 
    while True:
        a, nome_jogador, gols = sorteio_jogador()
        roleta_sorteio(a)
        lin()
        print(f"O jogador sorteado foi: {nome_jogador}")
        lin()
        escolha = menu_escolha(gols)
        s += 1
        if escolha is None:
            break
        estatisticas[nome_jogador] = escolha
        lin()
        print("Estatísticas atualizadas:")
        for jogador, gols in estatisticas.items():
            print(f"{jogador}: {gols} gols")
        lin()
        if s >= 3:
                total_gols = sum(estatisticas.values())
                print(f"Total de gols acumulados: {total_gols}")
                lin()
                if total_gols > 5000:
                    print("PARABENS VOCE GANHOU!!")
                break
    lin()
    print("Estatísticas Finais:")
    for jogador, gols in estatisticas.items():
        print(f"{jogador}: {gols} gols")
    lin()
