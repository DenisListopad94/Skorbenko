"""
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"
﻿ и выведите полученные строки.
"""

import re

strings = ["I am a human",
        "She is a human too",
        "We are all humans"]

for string in strings:
    new_string = re.sub(r'human', 'computer', string)
    print(new_string)