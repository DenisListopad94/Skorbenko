import re

def find_cat_substrings(s):
    substrings = re.findall(r'\b\wcat\w\b', s)
    return substrings