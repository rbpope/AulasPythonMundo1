v = int(input('Qual a velocidade do carro? '))
if v > 80:
    ve = int(v - 80)
    multa = float(ve*7.0)
    print('Você está {}Km/h acima do limite de velocidade e foi multado em R${:.2f}!'.format(ve, multa))
else:
    print('Ok')
