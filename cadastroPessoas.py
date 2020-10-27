# Criar um programa para cadastrar diversas pessoas
# Cada pessoa deverá ser um dicionário dentro de uma lista

# Entrada de dados:
# nome
# sexo
# idade

# Saída de dados :
# Quantos pessoas foram cadastradas
# A média de idade delas
# Quais foram as mulheres cadastradas
# Quais pessoas possuem mais que a idade média.

lista = []
cfem = idades = 0
while True :
    pessoa = {} # cria / zera o dicionário
    pessoa['nome'] = input('Nome:  ')
    while True:
        sexo = input('Insira o sexo [M para masculino / F para feminino:  ').lower()
        if sexo == 'm':
            pessoa['sexo'] = 'masculino'
            break
        elif sexo == 'f' :
            pessoa['sexo'] = 'feminino'
            cfem += 1
            break
    pessoa['idade'] = int(input('Idade:  '))
    idades += pessoa['idade']
    op = input('Deseja continuar? [S para sim]  ').lower()[0]
    lista.append(pessoa)
    #pessoa.clear() para zerar o dicionário
    if op != 's' :
        break

media = idades/len(lista)

print(f'\nForam cadastradas {len(lista)} pessoas.')
print(f'\nA média das idades é {media:.1f} anos.')
print(f'\nForam as mulheres cadastradas: ', end='')

for c in lista :
    if c['sexo'] == 'feminino' :
        if cfem > 2 :
            print(f'{c["nome"]}, ', end='')
        elif cfem == 2 :
            print(f'{c["nome"]} e ', end='')
        else:
            print(f'{c["nome"]}.')
        cfem -= 1

print(f'\nPossuem idade acima da média:')

for c in lista :
    if c['idade'] > media :
        print(f'\t{c["nome"]} com {c["idade"]} anos de idade.')
print()
