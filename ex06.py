# 6) Desenvolva um programa que receba como entrada do usuário as medidas de três lados de
# um triângulo. O programa deverá retornar como saída qual o tipo do triângulo, de acordo com
# as regras:
# • Triângulo Equilátero possui os três lados com as mesmas medidas.
# • Triângulo Escaleno possui os três lados diferentes
# • Triângulo Isósceles possui dois lados iguais
# Deve-se ainda verificar se as medidas formam um triângulo. Três medidas formam um triângulo
# quando a soma de dois lados for maior do que um terceiro lado.

print('informe a medidas dos lados de um triângulo')

lado1 = float(input('lado 1: '))
lado2 = float(input('lado 2: '))
lado3 = float(input('lado 3: '))

if lado1 + lado2 > lado3 and lado2 + lado1 > lado3 and lado3 + lado2 > lado1:
    if lado1 == lado2 and lado2 == lado3:
        print('é um Triângulo Equilátero!')

    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('é um Triângulo Escaleno!')

    else:
        print('é um Triângulo Isósceles!')
else:
    print('não é um Triângulo!')
