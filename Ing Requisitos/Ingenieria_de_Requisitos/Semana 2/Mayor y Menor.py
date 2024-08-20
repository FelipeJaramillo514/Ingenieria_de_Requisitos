Valor_A = float(input('Digita tu primer valor:'))
Valor_B = float(input('Digita tu segundo valor:'))

if Valor_A > Valor_B:
    print(Valor_A, 'es mayor que', Valor_B)
elif Valor_A == Valor_B:
    print(Valor_A,'=', Valor_B)
elif Valor_B == Valor_A:
    print(Valor_B,'=', Valor_A)
else:
    print(Valor_A, 'es menor que', Valor_B)