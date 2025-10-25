import sys
import os

# Добавляем путь к папке src
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка", yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))