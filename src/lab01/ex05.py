fio = input('Введите ФИО')
fio = fio.split()
initials = [fio[i][0] for i in range(len(fio))]
initials = ''.join(initials)

fio = ''.join(fio)
symbols = len(fio)

print(f'Инициалы: {initials}.')
print(f'Длина Символов: {symbols}')