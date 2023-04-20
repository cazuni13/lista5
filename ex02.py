# 2) Desenvolva um programa que leia um número inteiro. Se o número informado for positivo,
# imprimir sua raiz quadrada; se for negativo, o quadrado do número

num = int(input('informe um número positivo ou negativo: '))

if num > 0:
    raiz = (num ** 0.5)
    print(f'a raiz quadrada de número informado é {raiz}')

elif num < 0:
    quadrado = (num ** 2 )
    print(f'o quadrado do número é {quadrado}')

else:
    print('o número é neutro')
