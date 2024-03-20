total_segundos = int(input('Digite a quantidade de segundos: '))

dias = total_segundos // (24 * 3600)
horas = (total_segundos % (24 * 3600)) // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

print(f'Dias: {dias}')
print(f'Horas: {horas}')
print(f'Minutos: {minutos}')
print(f'Segundos:{segundos}')
