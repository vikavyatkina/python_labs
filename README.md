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


## Лабораторная работа 3
### Задание А 
### №1
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold == True:
        text = text.casefold()
        #приводим к нижнему регистру
    if yo2e == True:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
        #заменяем ё и Ё
    simbols = {'\t', '\r', '\n'}
    for i in simbols:
        text = text.replace(i, ' ')
    while '  ' in text: #вырезаем повторяющиеся пробелы
        text = text.replace('  ', ' ')
    text = text.strip()

    return text
```
![картинка1](./images/lab03/A1.png)

### №2
```python
def tokenize(text: str) -> list[str]:
    text_def = []
    i = 0
    while i < len(text):
        if text[i] == '-':
            if i > 0 and i < len(text) - 1: #если он не с краю
                if (text[i-1].isalnum() or text[i-1] == '_') and (text[i+1].isalnum() or text[i+1] == '_'):
                    text_def.append('_') #замена с дефиса на _
        else:
            text_def.append(text[i])
        i += 1
    text_def = ''.join(text_def) + ' '
    slovo = ''
    res = []
    for x in text_def:
        if x.isalnum() or x == '_':
            slovo += x
        else:
            if len(slovo) != 0:
                slovo = slovo.replace('_', '-') #обратно возвращаем дефисы
                res.append(slovo) #добавляем слово
                slovo = '' #освобождаем ячейку для следующего слова
    return res
```
![картинка1](./images/lab03/A2.png)

### №3-№4
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    res = {}
    for i in tokens:
        res[i] = res.get(i,0) + 1
    sorted_res = sorted(res.items(), key = lambda i: (i[0], i[1]))
    return dict(sorted_res)


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    c = list(count_freq(freq).items())
    return c[:n]
```

![картинка1](./images/lab03/A3.png)

### Заадание В
```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.lib.text import*

text = sys.stdin.read()

textn = text

text = normalize(text)
text = tokenize(text)
textn = text
top = top_n(count_freq(text), n = 5)
text = top_n(count_freq(text))


print(f"Всего слов: {len(textn)}")
print(f"Уникальных слов: {len(text)}")
print("Топ-5:")
for word, count in top:
    print(f"{word}: {count}")
```
![картинка1](./images/lab03/B.png)



## Лабораторная работа 4
### А
```python
import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    p = Path(path)

    if p.exists() == False:
        raise FileNotFoundError
    
    return p.read_text(encoding=encoding)

def ensure_parent_dir(path: str | Path) -> None:

    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:

    row_list = list(rows)

    if row_list:

        first_length = len(row_list[0])

        for i, row in enumerate(row_list):

            if len(row) != first_length:

                raise ValueError()
    ensure_parent_dir(path)

    p = Path(path)

    with p.open("w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)

txt = read_text("data/input.txt")  # должен вернуть строку
write_csv([("word","count"),("test",3)], "data/check.csv")  # создаст CSV

```

![картинка1](./images/lab04/test1.png)

## B
```python
import sys   
sys.path.append('C:/Users/ravm7/OneDrive/Рабочий стол/python_labs/python_labs/src')
from lib.text import normalize, tokenize, count_freq, top_n
from lib.io_txt_csv import read_text, write_csv, write_text


txt = read_text('data/lab04/input.txt')
txt = tokenize(normalize(txt))
txt_counts = top_n(count_freq(txt))
print('Всего слов:', len(txt))
print('Уникальных слов:', len(set(txt)))
print('Топ-5:')
for i in txt_counts:  
    print( f'{i[0]}:{i[1]}') 

write_csv(txt_counts, 'data/lab04/report.csv', ("word","count"))
```
![картинка1](./images/lab04/test2.png)


## Лабораторная работа 5
### Задание А
json to csv
```python
from pathlib import Path
import json
import csv
import sys
sys.path.append('C:/Users/ravm7/"Рабочий стол"/python_labs/python_labs')

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_path = Path(json_path)   # Создаем путь к файлу - Path-объект
    
    if not json_path.exists():   # Явная проверка существования пути
        raise FileExistsError('Путь не найден')

    with open(json_path, 'r', encoding='utf-8') as json_file:
        try:
            data_json = json.load(json_file)

        except json.JSONDecodeError:   #файл невозможно загрузить в формате JSON
            raise ValueError("Пустой JSON или неподдерживаемая структура")
        
        except not data_json:  # Явная проверка существования файла
            raise FileNotFoundError("Файл не найден")
        
        except not isinstance(data_json, list):
            raise ValueError('Файл не JSON формата: не список словарей')
        
        except not all(isinstance(row, dict) for row in data_json):
            raise ValueError('Файл не JSON формата: в списке не словари')
    '''
    Работаем с CSV-файлом, записывая в него данные из загруженного ранее JSON-файла.
    '''

    csv_path = Path(csv_path)

    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data_json[0].keys()) # Записывает список словарей, заголовок - ключи словарей
        writer.writeheader()
        writer.writerows(data_json) # Записываем данные построчно
```
![картинка1](./images/lab05/image1.png)
![картинка1](./images/lab05/image2.png)

csv to json

```python
from pathlib import Path
import json
import csv
import sys
sys.path.append('C:/Users/ravm7/"Рабочий стол"/python_labs/python_labs')

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """

    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError('Файл не найден')
    
    if csv_path.suffix != '.csv':
            raise ValueError("Неверный тип файла")
    '''
    Работаем с открытым CSV-файлом, пробуем читать как список словарей и отлавливаем ошибки.
    '''
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        try:
            data_csv = csv.DictReader(csv_file)

        except data_csv.fieldnames is None:
            raise ValueError('Отсутствуют заголовки')
        
        if len(list(data_csv)) == 0:
             raise ValueError("Пустой файл")
        data_csv = list(data_csv) # Создаёт список данных, сохраняем считанные данные

    json_path = Path(json_path)
    '''
    Работаем с JSON-файлом, загружая в него данные из CSV_файла.
    '''
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(json.dump(data_csv, json_file, ensure_ascii=False, indent=2))
        '''
        data_csv - что записываем
        json_file -  куда записываем
        ensure_ascii=False - корректная работа с кириллицей
        indent=2 - красивый вывод
        '''
```
![картинка1](./images/lab05/image3.png)
![картинка1](./images/lab05/image4.png)

### Задание B
```python
from pathlib import Path
import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter # Утилита openpyxl для получения буквы столбца таблицы

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """

    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    if not csv_path.exists():  # Явная проверка существования файла
        raise FileNotFoundError('Файл не найден')
    
    if not xlsx_path.exists():  # Явная проверка существования файла
        raise FileNotFoundError('Файл не найден')
    
    if csv_path.suffix != '.csv':
            raise ValueError("Неверный тип файла")
    '''
    Работаем с CSV-файлом, читаем из него информацию и проверяем на наличие ошибок. Если они есть - они всплывают.
    '''
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        csv_file = list(reader) # Сохраняем считанные данные в список
        if len(csv_file) == 0:
             raise ValueError("Пустой файл")
        
        if not reader.fieldnames:
             raise ValueError('Файл не содержит заголовков')
        
        wb = Workbook()      # Создаем рабочую книгу
        ws = wb.active       # Создаём в ней новый лист
        ws.title = "Sheet1"  # Называем его

        ws.append(reader.fieldnames)  # Добавляем заголовок
        for row in csv_file:
            ws.append([row[field] for field in reader.fieldnames])  # В каждую строку таблицы добавляем соответствующую ей информацию
        
        for column in ws.columns:   # Равняем всё по ширине, 8 - минимум
            max_length = 8
            column_letter = get_column_letter(column[0].column)
            for cell in column:
                max_length = max(len(str(cell.value)), max_length)

            ws.column_dimensions[column_letter].width = max_length
            

    wb.save(xlsx_path)  # Сохраняем все изменения в указанном пути
```
![картинка1](./images/lab05/image5.png)
![картинка1](./images/lab05/image6.png)
