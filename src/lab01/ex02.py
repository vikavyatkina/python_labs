a = float(input('Введите число').replace(',', '.'))
b = float(input('Введите число').replace(',', '.'))
s = a + b
av =round(s / 2, ndigits = 2)
print(f'sum = {s}; avg = {av}')
