import random
import math
import time

def main():  
    nome_jogador = input('Olá, como você se chama? ')
    print(f'Que nome legal, {nome_jogador}!')
    print(f'Vamos ver contra quem você ira lutar!')
    inimigos = ['Goblin', 'Ciclope', 'Golem']
    escolha_inimigo = random.choice(inimigos)
    print(f'Você está contra um {escolha_inimigo}!')
    if escolha_inimigo == 'Goblin':
        print('OBS: Os goblins possuem baixa vida, porém alta chance crítica!')
        vida_CPU = 25
        critmin = 17
        critmax = 20 #Necessita rolar exatamente 20 para o crítico
        danomin = 4
        danomax = 8
        acertomin = 1
        acertomax = 10 #Se rolar acima de 7, ele erra
    elif escolha_inimigo == 'Ciclope':
        print('OBS: Os Ciclopes possuem alto dano, porém baixa precisão!')
        vida_CPU = 40
        critmin = 1
        critmax = 20
        danomin = 10
        danomax = 16
        acertomin = 1
        acertomax = 20
    elif escolha_inimigo == 'Golem':
        print('OBS: Os golems possuem uma vida elevada, porém um baixo dano')
        vida_CPU = 60
        critmin = 1
        critmax = 20
        danomin = 2
        danomax = 6
        acertomin = 1
        acertomax = 10
         
    vida_jogador = 40
    mana_jogador = 20
    while True:
        print('-' * 30)
        print('Seu turno!')
        print('-' * 30)
        while True:
            print(f'O que você deseja fazer? Você possuí {vida_jogador} de vida e {mana_jogador} de mana.\nSeu oponente possuí {vida_CPU} de vida.')
            escolha1 = input('1- Atacar\n2- Defender\n3- Conjurar uma magia\n')
            if escolha1 not in ['1', '2', '3']:
                print('Insira apenas números válidos!')
            else:
                break

#escolha_CPU vem antes, pois caso contrário ele não consegueria defender do jeito que quero.
#Posso consertar isso depois fazendo um sistema de "speed", mas aí eu teria que pensar mais.
        defesa_CPU = False
        escolha_CPU = random.randint(1,10)
        if escolha_CPU > 8:
            defesa_CPU = True

        if escolha1 == '1':
            acertou = random.randint(1,10)
            defesa = False
            if acertou <= 7:
                dano_jogador = random.randint(3,6)
                critico_jogador = random.randint(1,20)
                if critico_jogador == 20:
                    dano_jogador *= 2
                if defesa_CPU == True:
                    dano_jogador //= 2
                vida_CPU -= dano_jogador
                if critico_jogador == 20:
                    print(f'Você atinge seu oponente. ACERTO CRÍTICO! Você causou {dano_jogador} de dano, deixando seu oponente com {vida_CPU} de vida.')
                else:
                    print(f'Você atinge seu oponente, Causando {dano_jogador} de dano e o deixando com {vida_CPU} de vida!')
            elif acertou >= 8:
                print('Você erra seu oponente!')
        elif escolha1 == '2':
            defesa = True
            print('Você defende!')
        elif escolha1 == '3':
            defesa = False
            while True:
                escolha_magia = input('Qual magia você quer conjurar?\n1- Bola de fogo(-5 de mana)\n2- Raios(-10 de mana)\n3- Canalizar(-0 de mana)\n')
                if escolha_magia not in ['1', '2', '3']:
                    print('Escolha apenas mágicas válidas!')
                else:
                    break
            if escolha_magia == '1':
                if mana_jogador < 5:
                    print('Você levanta suas mãos para conjurar uma magia, porém saem somente faíscas. Talvez você tenha esquecido quanto de mana possuía?')
                else:
                    mana_jogador -= 5
                    dano_jogador = random.randint(5,8)
                    critico_jogador = random.randint(1,20)
                    if critico_jogador == 20:
                        dano_jogador *= 2
                    vida_CPU -= dano_jogador
                    if critico_jogador == 20:
                        print(f'Você conjura uma bola de fogo e atira em seu inimigo. ACERTO CRÍTICO! Você causou {dano_jogador} de dano, deixando seu oponente com {vida_CPU} de vida.')
                    else:
                        print(f'Você conjura uma bola de fogo e atira em seu inimigo, causando {dano_jogador} de dano a ele e o deixando com {vida_CPU} de vida!')
            elif escolha_magia == '2':
                if mana_jogador < 10:
                    print('Você levanta suas mãos para conjurar uma magia, porém saem somente faíscas. Talvez você tenha esquecido quanto de mana possuía?')
                else:
                    mana_jogador -= 10
                    atingiu_mais = random.randint(1,10)
                    dano_jogador = random.randint(3,5)
                    critico_jogador = random.randint(1,20)
                    if critico_jogador == 20:
                        dano_jogador *= 2
                    vida_CPU -= dano_jogador
                    if critico_jogador == 20:
                        print(f'Você conjura raios que caem dos céus e atingem seu oponente. ACERTO CRÍTICO! Você causou {dano_jogador} de dano, deixando seu oponente com {vida_CPU} de vida.')
                    else:
                        print(f'Você conjura raios que caem dos céus e atingem seu oponente, causando {dano_jogador} de dano e o deixando com {vida_CPU} de vida!')
                    if atingiu_mais <= 6:
                        dano_jogador = random.randint(3,5)
                        critico_jogador = random.randint(1,20)
                        if critico_jogador == 20:
                            dano_jogador *= 2
                        vida_CPU -= dano_jogador
                        if critico_jogador == 20:
                            print(f'Os raios atingem seu oponente mais uma vez. ACERTO CRÍTICO! Você causou {dano_jogador} de dano, deixando seu oponente com {vida_CPU} de vida.')
                        else:
                            print(f'Os raios atingem seu oponente mais uma vez, o causando {dano_jogador} de dano e o deixando com {vida_CPU} de vida!')
            elif escolha_magia == '3':
                recuperacao_mana = random.randint(5,10)
                mana_jogador += recuperacao_mana
                print(f'Você recupera {recuperacao_mana} de mana, ficando com {mana_jogador} no total!')
            

#Checagem de morte, caso o jogador mate o CPU antes do turno dele.
        if vida_CPU <= 0:
            print(f'Você venceu! Parabéns, {nome_jogador}!')
            break
#Turno da CPU
        print('-' * 30)
        print('Vez da CPU!')
        print('-' * 30)
        if escolha_CPU <= 8:
            acertou_CPU = random.randint(acertomin, acertomax)
            defesa_CPU = False
            if acertou_CPU <= 7:
                dano_CPU = random.randint(danomin,danomax)
                critico_CPU = random.randint(critmin, critmax)
                if critico_CPU == 20:
                    dano_CPU *= 2
                if defesa == True:
                    dano_CPU //= 2
                if critico_CPU == 20:
                    print(f'Ele te atingiu. ACERTO CRÍTICO! Você perde {dano_CPU} de vida.')
                else:
                    print(f'Ele te atingiu! Causando {dano_CPU} de dano.')
                vida_jogador -= dano_CPU
            elif acertou_CPU >= 8:
                print('Ele te errou!')
        elif escolha_CPU > 8:
            print('Ele defende!')

#Chegagem de morte do player, já que só é possível ele tomar dano
#Após o turno do CPU, isso é feito logo após o dito turno.
        if vida_jogador <= 0:
            print(f'Que pena, você perdeu.')
            break







if __name__ == '__main__':
    while True:
        main()
        jogar_novamente = int(input('Quer jogar novamente?\n1- Sim\n2- Não\n'))
        if jogar_novamente == 2:
            break


