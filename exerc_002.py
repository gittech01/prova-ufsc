"""

Questão 2 (2.1)
Codificar um algoritmo que processa uma string que possua a seguinte composição:
Sendo: <nome_pessoa>#<data_nascimento>#<data_falecimento>#<local_nascimento>

a) Observa cuidadosamente e replique a formatação esperada para as saídas

b) Os exemplos de entrada mostrados acima estão disponíveis no arquivo string-exemplo-2023.txt.
Para testar, atribua as strings directamente a uma variável dentro do código. O texto deverá ser copiado apartir do
início da linha, tal como mostra na prova.

c) Para o cálculo da idade do falecido desconsidere os meses, execute uma subtração simples entre os anos.

d) Nos cálculos com o mês fevereiro, verifique se os anos são bissextos (pesque sobre como fazer isso) e então
considere 28 o 29 dias.

Ex.: edson    #   13/11/1283   #-#Sao Paulo


"""

from pprint import pprint

meses_ano =  [
    'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

dias_meses = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:

    # interage com o usuario para pegar as informacoes:
    infos = input('Digite o Nome, Data Nascimento, Data Falecimento e o Local de Nascimento separados por "#": ')

    # List comprehension:
    list_infos = [info.strip() for info in infos.split('#')]

    # desempacotar lista:
    nome_pessoa, data_nascimento, data_falecimento, local_nascimento = list_infos
    dia_nascimento, mes_nascimento, ano_nascimento = [int(value) for value in data_nascimento.split('/')]
    dia_falecimento, mes_falecimento, ano_falecimento = [int(value) for value in data_falecimento.split('/')]

    # calcular quantos viveu:
    idade_ao_falecer = ano_falecimento - ano_nascimento

    # definir o mês de nascimento e falicimento:
    mes_nasc = meses_ano[mes_nascimento - 1]
    mes_fal = meses_ano[mes_falecimento - 1]

    # definir o maior dia do mês de nascimento e falicimento:
    dia_mes_nasc = dias_meses[mes_nascimento - 1]
    dia_mes_fal = dias_meses[mes_falecimento - 1]

    # definir o ultimo dia do mês de nascimento e falicimento:
    ultimo_dia_mes_nasc = 0
    ultimo_dia_mes_fal = 0



    if 1<= mes_nascimento <= 12 and 1<= mes_falecimento <= 12:  # valida se os meses estão dento do intervalo de 1 a 12
        if ano_nascimento % 400 == 0 or (ano_nascimento % 4 == 0 and ano_nascimento % 100 != 0):    # valida ano bissexto
            if mes_nasc == 'fevereiro':
                if 1 <= dia_nascimento <= dia_mes_nasc[1]:
                    ultimo_dia_mes_nasc = dia_mes_nasc[1]
                else:
                    print(f'Data de nascimento {data_nascimento} ... INVÁLIDA!!!')
                    continue
            if mes_nasc != 'fevereiro':
                if 1 <= dia_nascimento <= dia_mes_nasc:
                    ultimo_dia_mes_nasc = dia_mes_nasc
                else:
                    print(f'Data de nascimento {data_nascimento} ... INVÁLIDA!!!')
                    continue
        else:
            if mes_nasc == 'fevereiro':
                if 1 <= dia_nascimento <= dia_mes_nasc[0]:
                    ultimo_dia_mes_nasc = dia_mes_nasc[0]
                else:
                    print(f'Data de nascimento {data_nascimento} ... INVÁLIDA!!!')
                    continue
            if mes_nasc != 'fevereiro':
                if 1 <= dia_nascimento <= dia_mes_nasc:
                    ultimo_dia_mes_nasc = dia_mes_nasc
                else:
                    print(f'Data de nascimento {data_nascimento} ... INVÁLIDA!!!')
                    continue

        if ano_falecimento % 400 == 0 or (ano_falecimento % 4 == 0 and ano_falecimento % 100 != 0):
            if mes_fal == 'fevereiro':
                if 1 <= dia_falecimento <= dia_mes_fal[1]:
                    ultimo_dia_mes_fal = dia_mes_fal[1]
                else:
                    print(f'Data de nascimento {data_falecimento} ... INVÁLIDA!!!')
                    continue
            if mes_fal != 'fevereiro':
                if 1 <= dia_falecimento <= dia_mes_fal:
                    ultimo_dia_mes_fal = dia_mes_fal
                else:
                    print(f'Data de nascimento {data_falecimento} ... INVÁLIDA!!!')
                    continue
        else:
            if mes_fal == 'fevereiro':
                if 1 <= dia_falecimento <= dia_mes_fal[0]:
                    ultimo_dia_mes_fal = dia_mes_fal[0]
                else:
                    print(f'Data de nascimento {data_falecimento} ... INVÁLIDA!!!')
                    continue
            if mes_fal != 'fevereiro':
                if 1 <= dia_falecimento <= dia_mes_fal:
                    ultimo_dia_mes_fal = dia_mes_fal
                else:
                    print(f'Data de nascimento {data_falecimento} ... INVÁLIDA!!!')
                    continue
    else:
        print('Data INVÁLIDA!!!')

    # impressão da Biografia
    print("#" * 80)
    print('Biografia'.center(80))
    print("#" * 80)
    print()
    print('Nome Completo: ', nome_pessoa)
    print('Data de Nascimento: ', data_nascimento)
    print('Local de Nascimento: ', local_nascimento)
    print('Morte: ', data_falecimento)
    print(f'Idade ao Falecer: {idade_ao_falecer} anos')
    print('-' * 80)

    print(f'{nome_pessoa} nasceu em um ano', end=' ')
    if ano_nascimento % 2 == 0:
        print(f'par ({ano_nascimento}).')
    else:
        print(f'ímpar ({ano_nascimento}).')

    print(f'{nome_pessoa} morreu em um ano', end=' ')
    if ano_falecimento % 2 == 0:
        print(f'par ({ano_falecimento}).')
    else:
        print(f'ímpar ({ano_falecimento}).')

    dia_restante_n = ultimo_dia_mes_nasc - dia_nascimento
    if ano_nascimento % 400 == 0 or (ano_nascimento % 4 == 0 and ano_nascimento % 100 != 0):
        print(f'Quando {nome_pessoa} nasceu, faltavam {dia_restante_n} dias para último dia do mês {mes_nasc}.')
    else:
        print(f'Quando {nome_pessoa} nasceu, faltavam {dia_restante_n} dias para último dia do mês {mes_nasc}.')

    dia_restante_f = ultimo_dia_mes_fal - dia_falecimento
    if ano_falecimento % 400 == 0 or (ano_falecimento % 4 == 0 and ano_falecimento % 100 != 0):
        print(f'Quando {nome_pessoa} morreu, faltavam {dia_restante_f} dias para último dia do mês {mes_fal}.')
    else:
        print(f'Quando {nome_pessoa} morreu, faltavam {dia_restante_f} dias para último dia do mês {mes_fal}.')

    print('-' * 80)

    deseja_continuar = input('Informe qualquer alfnumerico pra continuar ou espaço/Enter pra encerrar: ')

    if not len(deseja_continuar.strip()):
        print('Programa Encerrado!')
        break

# var_teste = '          Sigmund Freud        #06/05/1856#23/09/1939#Império Austro-Hungaro'