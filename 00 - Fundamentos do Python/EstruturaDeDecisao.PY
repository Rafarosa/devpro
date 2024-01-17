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
num011 = float(input('Informe o primeiro número: '))
num022 = float(input('Informe o segundo número: '))
num033 = float(input('Informe o terceiro número: '))

if num011 > num022 and num011 > num033:
    print(f'Numero {num011} é maior')
elif num022 > num011 and num022 > num033:
    print(f'Numero {num022} é maior')
else:
     print(f'Numero {num033} é maior')
"""

"""
7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print("O maior número é", maior)
print("O menor número é", menor)

"""
"""
8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
produto_01 = float(input('Informe o primero preço encontrado: '))
produto_02 = float(input('Informe o segundo preço encontrado: '))
produto_03 = float(input('Informe o terceiro preço encontrado: '))

menor_preco = produto_01

if produto_02 < menor_preco:
    menor_preco = produto_02
if produto_03 < menor_preco:
    menor_preco = produto_03

print(f'O menor preço é {menor_preco}')
"""

"""
9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
num_ord_01 = float(input('informe o primeiro número: '))
num_ord_02 = float(input('informe o segundo número: '))
num_ord_03 = float(input('informe o terceiro número: '))

maior = num_ord_01
meio = num_ord_02
menor = num_ord_03

if num_ord_02 > maior:
    maior = num_ord_02
    meio = num_ord_01
if num_ord_03 > maior:
    maior = num_ord_03
    meio = num_ord_01
if num_ord_02 < menor:
    menor = num_ord_02
if num_ord_03 < menor:
    menor = num_ord_03

print("Os números em ordem decrescente são:", maior, meio, menor)
"""

"""
10 - Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""