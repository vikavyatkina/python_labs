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


def count_freq(tokens: list[str]) -> dict[str, int]:
    res = {}
    for i in range(len(tokens)):
        if tokens[i] in res:
            continue
        else:
            res[tokens[i]] = tokens.count(tokens[i])
    return res

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:n]