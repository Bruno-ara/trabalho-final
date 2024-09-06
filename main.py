import func
from time import sleep
func.limpar()
print('''
Como o jogo funciona?
A cada jogador sorteado, deve selecionar se quer seus gols duplicados, triplicados ou com valores da carreira.
Ao final, os gols serão somados para atigir a meta, se conseguir, parabéns, senão...''')
sleep(5)
func.jogar()
