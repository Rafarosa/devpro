import math
#pi = math.pi
#print(pi)
"""
1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
"""
print('Alo mundo')

"""
2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

"""
numero = int(input('Informe um número: '))
print(f'O número informado foi {numero}')

"""
3 - Faça um Programa que peça dois números e imprima a soma.
"""

pedir_num01 = int(input('informe o primeiro número: '))
pedir_num02 = int(input('informe o segundo número: '))

soma = pedir_num01 + pedir_num02

print(f'A soma dos número {pedir_num01} e {pedir_num02} é igual a {soma}')

"""
4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

nota_bi1 = float(input('Informa sua nota no primeiro bimestre: '))
nota_bi2 = float(input('Informa sua nota no segundo bimestre: '))
nota_bi3 = float(input('Informa sua nota no terceiro bimestre: '))
nota_bi4 = float(input('Informa sua nota no quarto bimestre: '))

media_bimestre = (nota_bi1 + nota_bi2 + nota_bi3 + nota_bi4) / 4

print(f'A media do ano foi {media_bimestre:.2f}')
"""
5 - Faça um Programa que converta metros para centímetros.
"""

valor_metros = float(input('informe o valor em metros a ser convertido: '))
converte_centimetors = valor_metros * 100

print(f'{valor_metros}m é igual a {converte_centimetors}cm')
"""
6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
raio = float(input('Informe o raio do circulo: '))

area_circulo = pi * raio**2

print(f'Com o Raio igual a {raio}, a área do circulo é igual a {area_circulo:.2f5}')

"""
7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

lado_quadrado = float(input('Informe o lado do quadaro: '))

area_quadrado= lado_quadrado**2

print(f'A área do quadrado é {2 * area_quadrado}')

"""
8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
Valor_hora = float(input('Informe o valor em R$ da sua hora trabalhada: '))
qtd_horas_mes = float(input('informe a quantidade de horas trabalhadas no mês: '))
"""

total_salario_mes = Valor_hora * qtd_horas_mes

print(f'Seu salário será de R${total_salario_mes:.2f}')

"""
9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
"""
C = 5 * ((F-32) / 9).
fah = float(input('informe a temperatua em graus Fahrenheit(◦F): '))

convert_fah_cel = 5 * ((fah - 32) / 9)

print(f'{fah}◦F equivalem a {convert_fah_cel:.2f}◦C')
"""
10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
cel = float(input('informe a temperatua em graus Celsius(◦F)'))
"""

convert_cel_fah = (cel * (9/5)) + 32

print(f'{cel}◦F equivalem a {convert_cel_fah:.2f}◦F')

"""
11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A)o produto do dobro do primeiro com metade do segundo .
B)a soma do triplo do primeiro com o terceiro.
C)o terceiro elevado ao cubo.
"""

num_int_1 = int(input('Informe o primeiro número interiro: '))
num_int_2 = int(input('Informe o segundo número interiro: '))
num_float_1 = float(input('Informe um número real: '))

questao_a = (2 * num_int_1) * (num_int_2 / 2)
questao_b = (3 * num_int_1) + num_float_1
questao_c = num_float_1 ** 3

print(f'A) o produto do dobro do primeiro com metade do segundo é {questao_a}')
print(f'B) a soma do triplo do primeiro com o terceiro é {questao_b}')
print(f'C)  terceiro elevado ao cubo é {questao_c:.2f}')

"""
12 - Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
"""
altura = float(input('Informe sua altura: '))

peso_ideal = (72.7 * altura) - 58

print(f'Seu peso ideal é {peso_ideal}')

"""
13 - Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
A) Para homens: (72.7*h) - 58
B) Para mulheres: (62.1*h) - 44.7
"""
altura_pessoa = float(input('Informe sua altura: '))

peso_ideal_h = (72.7 * altura_pessoa) - 58
peso_ideal_m = (62.1 * altura_pessoa) - 44.7

print(f'Peso ideal para homens é de {peso_ideal_h:.2f}Kg')
print(f'Peso ideal para mulheres é de {peso_ideal_m:.2f}Kg')

"""
14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
"""
peso = float(input('Informe quantos quilos de peixe você pescou: '))
regulamento = 50
excesso = (peso - regulamento) * 4

if excesso <= 0:
    print('Sem multa para o pagamento')
else:
    print(f'Sua multa é de R${excesso:.2f}')

"""
15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
A) salário bruto.
B) quanto pagou ao INSS.
C) quanto pagou ao sindicato.
D) o salário líquido.
E) calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
valor_hora_trabalhada = float(input('Informe o valor de sua hora trabalhada: R$'))
horas_trabalhadas_mes = str(input('Informe as horas trabalhadas no formato (HH:MM): '))
"""
horas, minutos = horas_trabalhadas_mes.split(':')
horas_trabalhadas_mes_inteiro = (int(horas) + (int(minutos) /60))

salario_bruto = valor_hora_trabalhada * horas_trabalhadas_mes_inteiro
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto -(ir + inss + sindicato)

print(f'+ Salário Bruto : {salario_bruto} R$')
print(f'- IR (11%) : {ir}R$')
print(f'- INSS (8%) : {inss}R$')
print(f'- Sindicato ( 5%) : {sindicato}R$')
print(f'= Salário Liquido : {salario_liquido}R$')
"""
17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
 - comprar apenas latas de 18 litros;
 - comprar apenas galões de 3,6 litros;
 - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
area_a_ser_pintada = int(input('Digite a área, em metros quadrados a ser pintada: '))  # area em metros quadrados
area_com_folga = area_a_ser_pintada * 1.1
litros_por_metro = 6
litros_a_serem_usados = area_com_folga / litros_por_metro
litros_por_lata = 18
numero_de_latas = math.ceil(litros_a_serem_usados / litros_por_lata)
valor_com_apenas_latas = numero_de_latas * 80
print(f'Você deverá usar {numero_de_latas} latas de 18 litros, no valor de R$ {valor_com_apenas_latas}')

litros_por_galao = 3.6
numero_de_galoes = math.ceil(litros_a_serem_usados / litros_por_galao)
valor_com_apenas_galoes = numero_de_galoes * 25
print(f'Você deverá usar {numero_de_galoes} galões de 3.6 litros, no valor de R$ {valor_com_apenas_galoes}')

# Compra de tinta otimizada por valor
numero_de_latas = math.floor(litros_a_serem_usados / litros_por_lata)
valor_de_latas = numero_de_latas * 80
litros_faltantes = litros_a_serem_usados % litros_por_lata
numero_de_galoes = math.ceil(litros_faltantes / litros_por_galao)
valor_com_galoes = numero_de_galoes * 25

valor_total = valor_de_latas + valor_com_galoes

print(f'Você deverá usar {numero_de_latas} latas de 18 litros mais {numero_de_galoes} galões de 3.6 litros, no valor de R$ {valor_total}')
