# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# кодирование
import codemodule
with open('input.txt', 'r') as text:
    for line in text:
        with open('output.txt', 'a') as data:
            data.write(codemodule.readcode(codemodule.readlist(line)) + '\n')