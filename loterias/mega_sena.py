def mega_sena():
    while True:
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

        print('\033[1;32;43mBoa sorte! 🍀🤞\033[m\n')
