"""
Дана строка, выведите все вхождения слов, начинающиеся на гласную букву.
"""

import re

s = "Apple banana "
matches = re.findall(r'\b[aeiouAEIOU]\w+', s)

for match in matches:
    print(match)
