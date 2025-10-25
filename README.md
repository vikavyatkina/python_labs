# python_labs

## Лабораторная работа 1

### Задание номер 1

```python
name = input('ИМЯ:')
age = int(input('ВОЗРАСТ:'))
print(f'Привет, {name}! Через год тебе будет {age + 1}.')
```
![картинка номер 1](./images/lab01/ex1.png)

### Задание номер 2

```python
a = float(input('Введите число').replace(',', '.'))
b = float(input('Введите число').replace(',', '.'))
s = a + b
av =round(s / 2, ndigits = 2)
print(f'sum = {s}; avg = {av}')
```
![картинка номер 2](./images/lab01/ex2.png)

### Задание номер 3
```python
price = float(input('Цена, ₽:'))
discount = float(input('Скидка, %:'))
vat = float(input('НДС, %:'))

base = price * ( 1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f'База после скидки: {base:.2f} ₽')
print(f'НДС: {vat_amount:.2f} ₽')
print(f'Итого к оплате: {total:.2f} ₽')
```
![картинка номер 3](./images/lab01/ex3.png)

### Задание номер 4
```python
m = int(input('Целые минуты'))
hours = m//60
minutes = m % 60
print(f'{hours}:{minutes:02d}')
```
![картинка номер 4](./images/lab01/ex4.png)

### Задание номер 5
```python
fio = input('Введите ФИО')
fio = fio.split()
initials = [fio[i][0] for i in range(len(fio))]
initials = ''.join(initials)

fio = ' '.join(fio)
symbols = len(fio)

print(f'Инициалы: {initials}.')
print(f'Длина Символов: {symbols}')
```
![картинка номер 5](./images/lab01/ex05.png)


## Лабораторная работа 2
### Задание А

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        return 'ValueError'
    return(min(nums), max(nums))
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    result = []
    m = -10 * 10
    nums = sorted(nums)
    for i in nums:
        if i > m:
            result.append(i)
            m = i
    return result
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(mat: list[list | tuple]) -> list:
    for a in mat:
        if not(isinstance(a, (list, tuple))):
            return 'TypeError'
    result = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            result.append(mat[i][j])
    return result 
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![картинка номер 1](./images/lab02/arraysimage.png)

### Задание B

```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat) == 0:
        return []
    for a in range(len(mat)):
        if len(mat[a]) != len(mat[0]):
            return 'ValueError'
    stroci = len(mat)
    colons = len(mat[0])
    result = []
    for i in range(colons):
        colons1 = [0]*stroci
        result.append(colons1)
    for s in range(stroci):
        for e in range(colons):
            result[e][s] = mat[s][e]
        return result
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    for a in range(len(mat)):
        if len(mat[a]) != len(mat[0]):
            return 'ValueError'
    sums = []
    for i in range(len(mat)):
        sums.append(sum(mat[i]))
    return sums
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat)==0:
        return []
    for a in range(len(mat)):
        if len(mat[a]) != len(mat[0]):
            return 'ValueError'
    sums = []
    for j in range(len(mat[0])):
        s = 0
        for i in range(len(mat)):
            s = s + mat[i][j]
        sums.append(s)
    return sums
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![картинка номер2](./images/lab02/matriximage.png)

### Задание C

```python
def format_record(rec: tuple[str, str, float]) -> str:
    if any(str(x)=='' for x in rec):
        return 'ValueError'

    fio=str(rec[0]).split()
    group=str(rec[1])
    gpa=f'{float(rec[2]):.2f}'
    fio1=''
    fam=0 

    for i in range(len(fio)):
        if fio[i]!='' and fam==0:
            first_let=str(fio[i])[0].upper() 
            fio1+=first_let+str(fio[i][1:])+' '
            fam=1
        elif fio[i]!='' and fam==1:
            first_let=str(fio[i])[0].upper()
            fio1 += first_let + '.'
    res=fio1+', гр. '+group+', GPA '+str(gpa)
    return res
r=("Иванов Иван Иванович", "BIVT-25", 4.6)
r2=("Петров Пётр", "IKBO-12", 5.0)
r3=("Петров Пётр Петрович", "IKBO-12", 5.0)
r4=("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
print(format_record(r))
print(format_record(r2))
print(format_record(r3))
print(format_record(r4))
```
![картинка номер 3](./images/lab02/tuplesimage.png)
