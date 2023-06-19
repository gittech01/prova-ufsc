"""

Questão 1 (2.0)
Escreva um programa que leia do teclado um número de conta-corrente com exatos 5 digitos (apresente mensagem de erro caso
a quantidade difere ou caso algum caracter não, seja digitado) a partir do número lido, o seu programa deverá
geral um dígito verificador para esta conta e imprimi-lo com o número de conta. O dígito verificador é cálculado com a
sgte sequência de passos:

a) Somar o número de conta com o seu inverso
b) Efetuar um somatório das mult de cada digitos do resultado anterior pela sua ordem posicional
c) Identificar o último dígito do resultado da mult. Este será o dígito verificador da conta.

Exemplo:
Dado a conta: 23456

a) soma = 23456 + 65432 = 88888
b) som_pro = 1*8 + 2*8 + 3*8 + 4*8 + 5*8
c) digito_verificador = 12[0]

"""

while True:
    conta = input('Digite o código da conta Conta-Corrente: ').strip()

    tamanho = 5 - len(conta)

    if conta.isdigit() and not tamanho:
        soma = str(int(conta) + int(conta[::-1]))
        mult_soma = 0

        for indice, digito in enumerate(soma):
            mult_soma += int(soma[indice]) * (indice + 1)
        else:
            digito_verificador = str(mult_soma)[-1]
            print(f'Conta Corrente: {conta}-{digito_verificador}')

            deseja_continuar = input('Informe qualquer alfnumerico pra continuar ou espaço/Enter pra encerrar: ')

            if not len(deseja_continuar.strip()):
                print('Programa Encerrado!')
                break

    else:
        print('Conta inválida!!!')

# True -> 1
# False -> 0
# str_ = ''
# lista = []
# tupla = (2,)
# valor = 0
#
# if str_:
#     print('entrei')
