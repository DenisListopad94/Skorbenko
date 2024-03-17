"""
Извлечь дату из строки. Формат даты dd –mm-yyyy
"""

import re

text = "Это пример строки с датой 28-02-2022 в формате dd-mm-yyyy"

pattern = r'\b\d{2}-\d{2}-\d{4}\b'

matches = re.findall(pattern, text)

if matches:
    date = matches[0]
    print("Извлеченная дата:", date)
else:
    print("Дата не найдена в тексте.")
