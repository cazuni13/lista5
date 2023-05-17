
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
