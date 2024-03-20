valor=input('Insira cinco digitos: ')

if len(valor) != 5:
    print('Insira cinco digitos.')
else:
    print(valor[0], valor[1], valor[2], valor[3], valor[4], sep="   ")
