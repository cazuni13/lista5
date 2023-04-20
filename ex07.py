media = float(input('informe sua média: '))

if media >= 9:
    print('sua classificação é: superior!')

elif 7 <= media <= 8.9:
    print('sua classificação é: médio superior!')

elif 5 <= media <= 6.9:
    print('sua classificação é: médio!')

elif 3 <= media <= 4.9:
    print('sua classificação é: médio inferior!')

elif 0.1 <= media <= 2.9:
    print('sua classificação é: inferior!')

else:
    print('você não tem rendimentos! :( ')
