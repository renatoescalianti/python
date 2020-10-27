# Crie um programa que sorteie dados para 'n' jogadores
# Armazene cada jogador em um dicionário.
# Cada jogador/dicionário será um item de uma lista.

# A entrada de dados será:
# quantidade de jogadores
# tamanho do dado (6,8, 20, etc)
# nome do jogador

# A saída deverá conter:
# Lista em ordem decrescente dos jogadores e dados sorteados
# Quais jogadores tiveram as maiores notas

from random import randint

n = int(input('Insira quantos jogadores:  '))
jogadores = []
print('Deseja inserir o nome dos jogadores?')
while True :
    inserir = input('[S/N]  ').lower()[0]
    if inserir == 's' :
        inserir = True
        break
    elif inserir == 'n' :
        inserir = False
        break
print()

if inserir == False :
    for c in range(n):
        jogadores.append({'nome': f'Jogador {c+1}', 'dado': randint(1,6)})

if inserir == True :
    for c in range(n):
        jogador = {}    # criar da primeira vez / limpar o dicionário nas demais
        jogador['nome'] = input(f'Qual o nome do jogador {c+1}:  ')
        jogador['dado'] = randint(1,6)
        jogadores.append(jogador)
    print()

ranking = sorted(jogadores, key = lambda i: (i['dado']), reverse=True)

for test in ranking :
    for k,v in test.items() :
        print(f'{v} tirou ' if k =="nome" else f'{v} no dado.\n', end='',)

print(f'\nO maior número sorteado foi {ranking[0]["dado"]} por:')
for x,y in enumerate(ranking) :
        if y['dado'] == ranking[0]['dado'] :
            print(f'{ranking[x]["nome"]}')
print()
