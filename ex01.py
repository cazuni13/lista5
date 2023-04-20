# 1) Construa um programa que receba dois números do usuário, e retorne como saída a diferença
# entre o maior e o menor.

num1 = float(input('informe um numero: '))
num2 = float(input('informe outro numero: '))

if num1 > num2:
    diferenca = num1 - num2

else:
    diferenca = num2 - num1
    
print(f'a diferença entre esses numeros é de {diferenca:.1f}')

