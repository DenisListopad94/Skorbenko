import re

strings = ["zzz", "zaz", "z1z", "zabcz", "zzzzz", "zaaaaz", "z123z"]

pattern = re.compile(r"z.{3}z")

for str_1 in strings:
    if re.search(pattern, str_1):
        print(str_1)