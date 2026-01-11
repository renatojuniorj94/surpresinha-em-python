#versão 2.0
import random
quant_num = 0

while True:
    loteria = int(input('🍀 Qual loteria deseja apostar? (0 para parar)\n'
                        '\033[32mMega-sena [1]\n\033[m'
                        '\033[34mQuina [2]\n\033[m'
                        '\033[35mLotofacil [3]\n\033[m'
                        '\033[38;2;255;165;0mLotomania [4]\n\033[m'))
    if loteria == 0:
        break
    if loteria < 0 or loteria > 4:
        print('Opção inválida!')
    if loteria == 1: # Mega-sena
        print('Você escolheu \033[32mMega-sena\033[m')
        quant_jogos = int(input('Quantos jogos deseja fazer? '))
        if quant_jogos == 0:
            break
        quant_num = int(input('Quantos números deseja escolher? [6 a 20] '))
        while quant_num < 6 or quant_num > 20:
            print("Número inválido! Tente novamente.")
            quant_num = int(input('Quantos números deseja escolher? [6 a 20] '))
        for num in range(quant_jogos):
            num_unicos = random.sample(range(1, 61), quant_num)
            num_unicos.sort()
            print(num_unicos)
        
        print('Boa sorte! 🍀🤞')
    if loteria == 2: # Quina
        print('Você escolheu \033[34mQuina\033[m')
        quant_jogos = int(input('Quantos jogos deseja fazer? '))
        if quant_jogos == 0:
            break
        quant_num = int(input('Quantos números deseja escolher? [5 a 15] '))
        while quant_num < 5 or quant_num > 15:
            print("Número inválido! Tente novamente.")
            quant_num = int(input('Quantos números deseja escolher? [5 a 15] '))
        for num in range(quant_jogos):
            num_unicos = random.sample(range(1, 81), quant_num)
            num_unicos.sort()
            print(num_unicos)
        print()
    if loteria == 3: # Lotofacil
        print('Você escolheu \033[35mLotofacil\033[m')
        quant_jogos = int(input('Quantos jogos deseja fazer? '))
        if quant_jogos == 0:
            break
        quant_num = int(input('Quantos números deseja escolher? [15 a 20] '))
        while quant_num < 15 or quant_num > 20:
            print("Número inválido! Tente novamente.")
            quant_num = int(input('Quantos números deseja escolher? [15 a 20] '))
        for num in range(quant_jogos):
            num_unicos = random.sample(range(1, 26), quant_num)
            num_unicos.sort()
            print(num_unicos)
        print()
    if loteria == 4: #Lotomania
        print('Você escolheu \033[38;2;255;165;0mLotomania\033[m')
        quant_jogos = int(input('Quantos jogos deseja fazer? '))
        if quant_jogos == 0:
            break
        for num in range(quant_jogos):
            num_unicos = random.sample(range(1, 101), 50)
            num_unicos.sort()
            print(num_unicos)

#Ordenando os números em ordem crescente
#num_unicos.sort()
#print(num_unicos)