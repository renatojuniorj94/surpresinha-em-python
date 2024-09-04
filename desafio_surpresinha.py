#versão 2.0
import random
quant_num = 0

while True:
    loteria = int(input('Qual loteria deseja apostar? (0 para parar)\n'
                        'Mega-sena [1]\n'
                        'Quina [2]\n'
                        'Lotofacil [3]\n'))
    if loteria == 0:
        break
    if loteria < 0 or loteria > 3:
        print('Opção inválida!')
    if loteria == 1:
        print('Você escolheu Mega-sena')
        quant_jogos = int(input('Quantos jogos deseja fazer? '))
        quant_num = int(input('Quantos números deseja escolher? [6 a 15] '))
        for num in range(quant_jogos):
            num_unicos = random.sample(range(1, 61), quant_num)
            num_unicos.sort()
            print(num_unicos)
        print()
    if loteria == 2:
        print('Você escolheu Quina')
        quant_jogos = int(input('Quantos jogos deseja fazer? '))
        quant_num = int(input('Quantos números deseja escolher? [5 a 15] '))
        for num in range(quant_jogos):
            num_unicos = random.sample(range(1, 81), quant_num)
            num_unicos.sort()
            print(num_unicos)
        print()
    if loteria == 3:
        print('Você escolheu Lotofacil')
        quant_jogos = int(input('Quantos jogos deseja fazer? '))
        quant_num = int(input('Quantos números deseja escolher? [15 a 20] '))
        for num in range(quant_jogos):
            num_unicos = random.sample(range(1, 26), quant_num)
            num_unicos.sort()
            print(num_unicos)
        print()

#Ordenando os números em ordem crescente
#num_unicos.sort()
#print(num_unicos)