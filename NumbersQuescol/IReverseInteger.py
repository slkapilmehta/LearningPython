def revInteger(num):
    rnum = 0
    if num == 0:
        print("enter a valid number")
        return -1
    elif num >0 and num <10:
        print("single digit number reverse is number itself")
        return num
    elif num >= 10:
        return (logic(num, rnum))
    elif num <0:
        num = num*-1
        return (logic(num, rnum))
    else:
        return -1

def logic(num, rnum):
    while num > 0:
        rnum = num % 10 + rnum * 10
        num = num // 10
    return rnum

num = 291.1
print(revInteger(int(num)))