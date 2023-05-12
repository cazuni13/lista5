print('leve em consideração estes cargos:')
print('1 - Testador' , '2- Analista de Testes' , '3 - Programador' , '4- Analista de Sistemas' , '5-dba')

valores = {
    '1': 20.00,
    '2': 35.00,
    '3': 45.00,
    '4': 40.00,
    '5': 50.00
}

funcao = input('Digite o número da funcao desempenhada (1-5): ')
hrs = float(input('Digite o número de horas trabalhadas: '))

salario = valores[funcao] * hrs

print(f'O salário do profissional é: R$ {salario:.2f}')

