def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError('Список пуст')
    return (min(nums), max(nums))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    result = []
    for i in mat:
        if isinstance(i, (list, tuple)):
            result.extend(i)
        else:
            raise TypeError('Элемент не подходит списку')
    return result

print('тест функции min_max')
numbers = input('Введите числа через пробел:')
if numbers:
    numbers_list = [float(x) for x in numbers.split()]
    try:
        result = min_max(numbers_list)
        print(f'Результат: {result}')
    except ValueError as e:
        print(f'Ошибка: {e}')
print('тест функции unique_sorted')
numbers = input('Введите числа через пробел:')
if numbers:
    numbers_list = [float(x) for x in numbers.split()]
    result = unique_sorted(numbers_list)
    print(f'Результат: {result}')
print('тест функции flatten')
print('Введите списки:')
lists_input = input('для flatten:')
if lists_input:
    try:
        lists = []
        for item in lists_input.split(']['):
            item = item.replace('[', '').replace(']','')
            if item:
                lists.append([float(x) for x in item.split(',')])
        result = flatten(lists)
        print(f'Результат: {result}')
    except Exception as e:
        print(f'Ошибка: {e}')