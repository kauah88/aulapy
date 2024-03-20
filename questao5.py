a=int(input('Insira o valor de a: '))
b=int(input('Insira o valor de b: '))
c=int(input('Insira o valor de c: '))

delta = b**2 - 4*a*c


if delta < 0:
    print('A equação não possui raizes reais.')
else:

    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    
    print('As raízes da equação são:')
    print(f'x ={x1}')
    print('x ={x2}')