# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.



def readlist(line):
    lst = list(line)
    code = ''
    count = 1
    for i in range(1, len(lst)):
        if i < (len(lst) - 1):
            if lst[i] == lst[i - 1]:
                count += 1
            elif lst[i] != lst[i - 1]:
                code += (str(count) + lst[i - 1])
                count = 1
        elif i == (len(lst) - 1):
            if lst[i] == lst[i - 1]:
                count += 1
                code += (str(count) + lst[i])
            elif lst[i] != lst[i - 1]:
                code += (str(count) + lst[i - 1])
    return code


def readcode(x):
    count = int(x[0])
    z = x[1]
    zipcode = ''
    for i in range(2, len(x) - 1, 2):
        if (x[i] == x[i - 2]) and (int(x[i]) == 1):
            count += 1
            z += x[i + 1]
        else:
            if len(z) == 1:
                zipcode += str(count) + z + x[i] + x[i + 1]
            else:
                zipcode += str(count * -1) + z + x[i] + x[i + 1]
            count = 0
            z = ''
    return zipcode


# кодирование

import decodemodule
with open('input_for_coding.txt', 'r') as text:
    for line in text:
        with open('output_from_coding.txt', 'a') as data:
            data.write(readcode(readlist(line)))

# декодирование
with open('output_from_coding.txt', 'r') as text:
    for line in text:
        with open('decoding.txt', 'a') as data:
            data.write(decodemodule.decode(line))