def custom_write(file_name, strings):
    strings_positions = {}
    num_string = 0
    file = open(file_name, 'w', encoding='utf-8')
    file.close()
    if isinstance(strings, list):
        for string in strings:
            num_string += 1
            file = open(file_name, 'a+', encoding='utf-8')
            strings_positions[(num_string, file.tell())] = string
            file.write(f'{string}\n')
            file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
