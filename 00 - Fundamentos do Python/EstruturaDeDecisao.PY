"""
1 - Faça um Programa que peça dois números e imprima o maior deles.
num01 = float(input('Informe o primeiro número: '))
num02 = float(input('Informe o segundo número: '))

if num01 > num02:
    print(f'{num01} é maior que {num02}')
else:
    print(f'{num02} é maior que {num01}')

"""

"""
2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
num03 = float(input('Informe um valor: '))

if num03 >= 0:
    print(f'{num03} é positivo!')
else:
    print(f'{num03} é negativo!')
"""

"""
3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = str(input('Informe a letra do sexo, F para feminino ou M para masculino: ')).upper()

if sexo == 'M':
  print('Masculino')
elif sexo == 'F':
  print('Feminino')
else:
  print('Sexo Inválido')
"""

"""
4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input('Informe a letra para validar se é uma vogal ou consoante: ')).upper()
vogal =  ['A','E','I','O','U']

if letra in vogal:
    print('vogal')
else:
    print('Consoante!')
"""

"""
5 - Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:

- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota_aluno_01 = float(input('Informe a primeira nota parcial: '))
nota_aluno_02 = float(input('Informe a segunda nota parcial: '))

media = (nota_aluno_01 + nota_aluno_02) / 2
print(f'Sua média é {media}')
if media < 7:
    print('Reprovado')
elif media >=7 and media < 10:
    print('Aprovado')
else:
    print('Aprovado com Distinção')
"""

"""
6 - Faça um Programa que leia três números e mostre o maior deles.
"""

"""
7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
"""
8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
"""
9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
"""
10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""