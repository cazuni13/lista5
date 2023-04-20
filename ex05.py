#5) Desenvolva um programa que receba três valores inteiros, e determine se o menor valor é
#par.

print('insira 3 valores')

num1 = int(input('número 1: '))
num2 = int(input('número 2: '))
num3 = int(input('número 3: '))

if num1 < num2 and num1 < num3:
    print(f'o menor número é {num1}')
    if num1 % 2 == 0:
        print('este número é par!')
    else:
        print('este número não é par!')

elif num2 < num1 and num2 < num3:
    print(f'o menor número é {num2}')
    if num2 % 2 == 0:
        print('este número é par!')
    else:
        print('este número não é par!')

else:
    print(f'o menor número é {num3}')
    if num3 % 2 == 0:
        print('este número é par!')
    else:
        print('este número não é par!')