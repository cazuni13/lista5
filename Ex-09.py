
indice = float(input('Informe o índice da poluição: '))

if indice >= 0.05 and indice <= 0.25:
    print('Índice de poluição dentro do aceitável.')
elif indice > 0.25 and indice <= 0.3:
    print('Indústrias do 1º grupo devem suspender suas atividades.')
elif indice > 0.3 and indice <= 0.4:
    print('Indústrias do 1° e 2º grupo devem suspender suas atividades.')
elif indice > 0.4:
    print('Os 3 grupos devem suspender suas atividades.')
else:
    print('Índice inválido.')

