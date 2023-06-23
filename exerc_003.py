"""
Questão 3 (2.0)

Crie um algoritmo que tome como entrada um dicionário criado diretamente no código.
Este dicionário deverá conter informação sobre atletas masculinos de elite que disputam a prova dos 100m rasos.

Formato do dicionário:

    {'nome sobrenome': [[tempos_float], ['nome sobre esposa', salario_esposa_float], bool]}
Ex.:dic_prova = {'Fulano da Silva': [[9.83, 9.92, 9.67], ['Maria Chiquinha Zubimba', 2230.00], True]}

Para cada atleta, estão associados:
  i) Seus três tempos mais recentes obtidos na prova dos 100m rasos.
 ii) Os nomes de suas esposas e os salários que cada uma delas recebe.
iii) Uma indicação sobre se o atleta já foi medalhista olímpico ou não.

O arquivo dic_prova_2.py, disponível no Moodle, contém um exemplo deste dicionário.
No entanto, seu programa deverá ser genérico, ou seja, deverá ser capaz de processar qualquer
dicionário construído neste formato.

Ao final, seu programa deverá apresentar as seguintes informações:
a) O nome e o pior tempo do atleta que possui o pior tempo entre todos.
b) O nome da esposa e o tempo do atleta que possui o melhor tempo.
c) A média total de todos os tempos dos medalhistas olímpicos.
d) O nome e a média dos tempos do atleta cuja esposa recebe o maior salário.
e) Os nomes do casal cuja esposa recebe o pior salário.
f) O somatório dos salários das esposas de todos os atletas.
g) O melhor e o pior tempo do não medalhista olímpico.
h) Os nomes do casal que possui a maior quantidade de letra somadas no seu nome.
i) Os nomes de todas as esposas ordenados alfabeticamente pelos últimos sobrenomes.
j) Uma lista de todos os nomes (atletas e esposas) organizados alfabeticamente em ordem inversa pelos primeiro nome.

"""

"""
sintaxe: 
        nome_dicionario = {'chave': 'valor'}
        
        Ex.: dic1 = {'nome': 'Edson', 'idade': 12, 'ensino_medio': True}
        
sintaxe de como acessar o valor do dicionario:

        nome_dicionario['chave'] ou nome_dicionario.get('chave')
        
        Ex.: dic1['nome'] # Edson
             dic1['ensino_medio'] # True
             
sintaxe para ver somente todos os valores ou todas as chaves:
        
        nome_dicionario.values()   --> Retorna uma lista contendo todos os valores.
        
        nome_dicionario.keys()   --> Retorna uma lista contendo todas as chaves. 


dic1 = {'nome': 'Edson', 'idade': 12, 'ensino_medio': True}

# print(dic1.keys())

# print(dic1['nome'])
# print(dic1.get('nome'))
# print(dic1['ensino_medio'])
       
"""

dic_prova = {

    'Fulano da Silva': [[9.83, 9.92, 9.67], ['Maria Chiquinha Zubimba', 2230.00], True],
    'Beltrano de Souza': [[9.69, 10.21, 9.77], ['Agrícola Beterraba Areia Leão', 1500.33], False],
    'Sicrano dos Santos': [[9.75, 9.90, 9.60], ['Lindolfa Celidônia Calafange de Tefé', 25000.25], False],
    'Nonô Sem Dente': [[9.80, 10.03, 9.98], ['Maria das Couves', 3050.00], False],
    'João Ninguém': [[9.73, 9.62, 9.59], ['Maricotinha Torquato Soares', 7200.47], True],
    'Simplício Simplório da Simplicidade Simples': [[9.63, 9.82, 9.0], ['Valesca Gertrudes Olissipa', 17495.36], False],
    'Kenquem que Ninguém Quer': [[10.74, 9.11, 9.80], ['Sandra Sandreca Suelissandra', 6890.00], True]

}


# a) O nome e o pior tempo do atleta que possui o pior tempo entre todos.
# nome e o menor tempo
nome_tempo = {}

for key in dic_prova.keys():
    nome_tempo[key] = min(dic_prova.get(key)[0])
else:
    pior_tempo = 0
    nome_atleta_com_pior_tempo = ''
    for indice, nome in enumerate(nome_tempo.keys()):

        if indice == 0:
            pior_tempo = nome_tempo[nome]
            continue

        if pior_tempo > nome_tempo[nome]:
            nome_atleta_com_pior_tempo = nome
            pior_tempo = nome_tempo[nome]

    print(nome_atleta_com_pior_tempo, pior_tempo)


# b) O nome da esposa e o tempo do atleta que possui o melhor tempo.
# nome e o menor tempo
nome_tempo = {}

for key in dic_prova.keys():
    nome_tempo[key] = max(dic_prova.get(key)[0])
else:
    maior_tempo = 0
    nome_esposa_atleta_com_maior_tempo = ''
    for indice, nome in enumerate(nome_tempo.keys()):

        if indice == 0:
            maior_tempo = nome_tempo[nome]
            continue

        if pior_tempo < nome_tempo[nome]:
            nome_esposa_atleta_com_maior_tempo = dic_prova.get(nome)[1][0]
            maior_tempo = nome_tempo[nome]

    print(nome_esposa_atleta_com_maior_tempo, maior_tempo)


# c) A média total de todos os tempos dos medalhistas olímpicos.
media = []

for key in dic_prova.keys():
    if dic_prova.get(key)[2]:
        media.append(
            sum(dic_prova.get(key)[0])/len(dic_prova.get(key)[0])
        )
else:
    media = sum(media)/len(media)

    print(f'Média: {media:.2f}')




