# Importações
from time import sleep

# funções

def menu(tamcédula_100, tamcédula_50, tamcédula_20, tamcédula_10):
    while True:
        print('-' * 42)
        print('MENU'.center(42))
        print('-' * 42)
        print('0 - Sair')
        print('1 - Sacar')
        print('-' * 42)
        while True:
            pergunta = int(input('Operação: '))
            if pergunta == 0:
                sleep(0.5)
                break
            elif pergunta == 1:
                sleep(0.5)
                break
            print('Valor inválido. Tente Novamente')
        if pergunta == 0:
            print('-' * 42)
            print('CAIXA FINALIZADO'.center(42))
            print('-' * 42)
            break
        elif pergunta == 1:
            print('-' * 42)
            print('SAQUE'.center(42))
            print('-' * 42)
            while True:
                valor = int(input('Quanto deseja sacar? '))
                if valor <= 1000:
                    break
                print('Limite de R$1000 reais.')
            print('Executando a operação.')
            sleep(0.5)
            print('Contando as notas.')
            sleep(0.5)
            total = valor
            cédula = 100
            tamcédula_100_cont = 0
            tamcédula_50_cont = 0
            tamcédula_20_cont = 0
            tamcédula_10_cont = 0
            if valor % 2 == 0:
                while True:
                    if cédula == 100:
                        if total >= 100:
                            if tamcédula_100 != 0:
                                total -= 100
                                tamcédula_100 -= 1
                                tamcédula_100_cont += 1
                            else:
                                tamcédula_100 += tamcédula_100_cont
                                cédula = 50
                        elif total >= 50:
                            if tamcédula_50 != 0:
                                total -= 50
                                tamcédula_50 -= 1
                                tamcédula_50_cont += 1
                            else:
                                cédula = 20
                        elif total >= 20:
                            if tamcédula_20 != 0:
                                total -= 20
                                tamcédula_20 -= 1
                                tamcédula_20_cont += 1
                            else:
                                cédula = 10
                        elif total >= 10:
                            if tamcédula_10 != 0:
                                total -= 10
                                tamcédula_10 -= 1
                                tamcédula_10_cont += 1
                            else:
                                print('Não há notas o suficiente')
                                tamcédula_50 += tamcédula_50_cont
                                tamcédula_20 += tamcédula_20_cont
                                tamcédula_10 += tamcédula_10_cont
                                tamcédula_100 += tamcédula_100_cont
                                break
                    elif cédula == 50:
                        if total >= 50:
                            if tamcédula_50 != 0:
                                total -= 50
                                tamcédula_50 -= 1
                                tamcédula_50_cont += 1
                            else:
                                tamcédula_50 += tamcédula_50_cont
                                cédula = 20
                        elif total >= 20:
                            if tamcédula_20 != 0:
                                total -= 20
                                tamcédula_20 -= 1
                                tamcédula_20_cont += 1
                            else:
                                cédula = 10
                        elif total >= 10:
                            if tamcédula_10 != 0:
                                total -= 10
                                tamcédula_10 -= 1
                                tamcédula_10_cont += 1
                            else:
                                print('Não há notas o suficiente')
                                break
                    elif cédula == 20:
                        if total >= 20:
                            if tamcédula_20 != 0:
                                total -= 20
                                tamcédula_20 -= 1
                                tamcédula_20_cont += 1
                            else:
                                cédula = 10
                        elif total >= 10:
                            if tamcédula_10 != 0:
                                total -= 10
                                tamcédula_10 -= 1
                                tamcédula_10_cont += 1
                            else:
                                print('Não há notas o suficiente')
                                break
                    elif cédula == 10:
                        if total >= 10:
                            if tamcédula_10 != 0:
                                total -= 10
                                tamcédula_10 -= 1
                                tamcédula_10_cont += 1
                            else:
                                print('Não há notas o suficiente')
                                tamcédula_50 += tamcédula_50_cont
                                tamcédula_20 += tamcédula_20_cont
                                tamcédula_10 += tamcédula_10_cont
                                tamcédula_100 += tamcédula_100_cont
                                break
                    if total == 0:
                        if tamcédula_100_cont != 0:
                            print(f'Retirado {tamcédula_100_cont} cédulas de 100 reais.')
                        if tamcédula_50_cont != 0:
                            print(f'Retirado {tamcédula_50_cont} cédulas de 50 reais.')
                        if tamcédula_10_cont != 0:
                            print(f'Retirado {tamcédula_20_cont} cédulas de 20 reais.')
                        if tamcédula_10_cont != 0:
                            print(f'Retirado {tamcédula_10_cont} cédulas de 10 reais.')
                        print(f'Sacado R${valor} reais.')
                        sleep(0.5)
                        break
            else:
                print('Houve um problema.')
                sleep(0.5)


# Notas

tamcédula_100 = 10
tamcédula_50 = 20
tamcédula_20 = 20
tamcédula_10 = 100

# Iniciar

menu(tamcédula_100, tamcédula_50, tamcédula_20, tamcédula_10)