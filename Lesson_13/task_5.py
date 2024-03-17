import re

s = "Строка с числами: 123, -45, 6.7, -8.9"
numbers = re.findall(r"[-+]?\d+\.\d+|[-+]?\d+", s)

for number in numbers:
    print(number)
