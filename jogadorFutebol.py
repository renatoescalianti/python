# Exercício:

# Faça um programa que aceite as entradas:
# nome
# partidas
# gols (em cada partida)
# total

# e produza uma saída:
# Nome do jogador e quantas partidas foram jogadas
# Total de gols feitos
# Quantos gols fez em cada partida.

jogador = {}
jogador['nome'] = input('Insira o nome do jogador: ')
jogador['partidas'] = int(input('Quantas partidas jogadas? '))
jogador['gols'] = []
jogador['total'] = 0
for p in range(0,jogador['partidas']) :
    jogador['gols'].append(int(input(f'Quantos gols na partida {p}? ')))

# a soma de gols poderia ter sido feita em somente um LOOP com o seguinte código.
'''
    gol = int(input('Gol na partida: '))
    jogador['total'] += gol
    jogador['gols'].append(gol)
'''
# com o uso do código acima, poderia ser suprimida as linhas 24 a 28

# foi feito um segundo FOR LOOP com o fim de estudar as estruturas de variáveis compostas e repetições
total = 0
for g in jogador['gols'] :
    total += g
jogador['total'] = total

print(f'O jogador {jogador["nome"]} jogo {jogador["partidas"]} partidas.')
print(f'Durante referidas partidas, fez o total de {jogador["total"]} gols:')

# como c = 0 é inicial, pode ser suprimido do código em Python
for c in range(jogador['partidas']) :
    print(f'\tNa partida {c+1} fez {jogador["gols"][c]} gols.')
