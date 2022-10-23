

def decode(x):
    lit = ''
    count = 0
    string = ''
    for i in range(len(x)):
        if x[i].isdigit() == True:
            num = int(x[i])
            continue
        elif x[i].isalpha() == True:
            lit += x[i]
            if i <= len(x) - 2:
                if x[i + 1].isalpha() == True:
                    count += 1
                    continue
                elif x[i + 1].isdigit() == True and x[i - 1].isalpha() == True:
                    count += 1
                    string += lit * (num //count)
                    count = 0
                    lit = ''
                elif x[i + 1].isdigit() == True and x[i - 1].isdigit() == True:
                    count = 1
                    string += lit * (num //count)
                    count = 0
                    lit = ''
            else:
                if x[i - 1].isalpha() == True:
                    count += 1
                    string += lit * (num // count)
                else:
                    count = 1
                    string += lit * (num // count)
    return string

