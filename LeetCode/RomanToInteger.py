def rti(num):
    total = 0
    if 'IV' in num:
        total = total + 4
        num = num.replace('IV', '')
    if 'IX' in num:
        total += 9
        num = num.replace('IX', '')

    if 'XL' in num:
        total += 40
        num = num.replace('XL', '')

    if 'XC' in num:
        total += 90
        num = num.replace('XC', '')

    if 'CD' in num:
        total += 400
        num = num.replace('CD', '')

    if 'CM' in num:
        total += 900
        num = num.replace('CM', '')
    for n in num:
        if n == 'I':
            total += 1
        elif n == 'V':
            total += 5
        elif n == 'M':
            total += 1000
        elif n == 'D':
            total += 500
        elif n == 'C':
            total += 100
        elif n == 'L':
            total += 50
        elif n == 'X':
            total += 10
    return total

num = "MCMXCIV"
print(rti(num))