# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# кодирование
with open('input.txt', 'r') as text:
    for line in text:
        count = 1
        code = ''
        lst = list(line)
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
                    code += ('1' + lst[i])

        print(code)
        with open('output.txt', 'a') as data:
            data.writelines(code)