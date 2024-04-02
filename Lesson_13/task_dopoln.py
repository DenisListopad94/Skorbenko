"""
Напишите регулярное выражение для поиска всех HTML тегов в тексте
"""

import re

text = " <h1>This is a paragraph</h1>   <body>This is a heading</body>   This is a division "

tags = re.findall(r'<.*?>', text)

for tag in tags:
    print(tag)
