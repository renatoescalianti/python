# Exercício
# Criar um código Python usando dicionário para calcular
# tempo restante de trabalho para aposentadoria.

# ENTRADA DE DADOS:
# nome
# ano de nascimento
# sexo
# ano do primeiro emprego

# Considerar regra 95/85 (idade+tempo de contribuição)

# Saída de dados:
# {} possui {} anos de idade, trabalhou {} anos e faltam {} para aposentar.

from datetime import datetime
ano = datetime.now().year

dicio = {}
dicio['nome'] = input('Nome: ')
dicio['ano de nascimento'] = int(input('Ano de nascimento: '))
dicio['sexo'] = 'não definido'
while dicio['sexo'] not in 'hm' :
    dicio['sexo'] = input('Sexo [H ou M]: ').lower()
dicio['ano do primeiro emprego'] = int(input('Ano do primeiro emprego: '))

idade = ano - dicio["ano de nascimento"]
if dicio['sexo'] == 'm' :
    aposentar = ( 85 - idade ) / 2
else :
    aposentar = ( 95 - idade ) / 2
trabalhou = ano - dicio['ano do primeiro emprego']
print(f'{dicio["nome"]} possui {idade} anos de idade.')
print(f'Trabalhou {trabalhou} anos e faltam {aposentar} anos para aposentar.')
