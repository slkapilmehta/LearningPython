def pNumber(number):
    rnum=0
    onumber = number
    while number != 0:
        rnum = number % 10 + rnum * 10
        number = number // 10
    print(rnum)
    print(onumber)
    if onumber == rnum:
        return True
    else:
        return False

number = 121
print(pNumber(number))