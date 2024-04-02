"""
Найти все слова, в которых есть хотя бы одна буква ‘b’
"""

import re

text = "I have a big black dog and a brown cat"

str_b = re.findall(r'\b\w*b\w*\b', text)

print(str_b)


