import re

phone_num = [
    '8901234567',
    '81234567890',
    '7654321098',
    '9345678901',
    '8998765432'
]

pattern = re.compile(r'^[89]\d{9}$')

for phone_number in phone_num:
    if pattern.match(phone_number):
        print(f'{phone_number} - Валидный номер')
    else:
        print(f'{phone_number} - Невалидный номер')
