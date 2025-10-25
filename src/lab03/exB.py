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


print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))