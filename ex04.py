# 4) Desenvolver um programa que receba como entrada três números. Determinar qual entre
# estes três números é o maior.

print('informe 3 números quaisquer')

num1 = float(input('número 1: '))
num2 = float(input('número 2: '))
num3 = float(input('número 3: '))

if num1 > num2 and num1 > num3:
    print(f'o maior número é {num1}')

elif num2 > num1 and num2 > num3:
    print(f'o maior número é {num2}')

else:
    print(f'o maior númro é {num3}')
