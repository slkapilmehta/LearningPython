def pNumber(number):
    rnum=0
    # if we need to check negative nummber without considering -ve sign, multiply number with -1
    # or convert it into string then remove -ve and proceed
    onumber = number
    while number > 0:
        rnum = number % 10 + rnum * 10
        number = number // 10
    print(rnum)
    print(onumber)
    if onumber == rnum:
        return True
    else:
        #for negative, it will return false
        return False

number = -121
print(pNumber(number))