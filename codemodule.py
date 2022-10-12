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
            count += int(x[i])
            z += x[i + 1]
        else:
            if len(z) == 1:
                zipcode += str(count) + z + x[i] + x[i + 1]
            else:
                zipcode += str(count * -1) + z + x[i] + x[i + 1]
            count = x[i]
            z = ''
    return zipcode

