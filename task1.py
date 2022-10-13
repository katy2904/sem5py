# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# кодирование
import codemodule
import decodemodule
with open('input_for_coding.txt', 'r') as text:
    for line in text:
        with open('output_from_coding.txt', 'a') as data:
            data.write(codemodule.readcode(codemodule.readlist(line)) + '\n')

# декодирование
with open('output_from_coding.txt', 'r') as text:
    for line in text:
        print(line)
        with open('decoding.txt', 'a') as data:
            data.write(decodemodule.decode(line) + '\n')