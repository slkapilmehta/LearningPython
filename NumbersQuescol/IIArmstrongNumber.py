#Q. Write a program to check if an integer is armstrong or not?

def armnum(num):
    sumNum = 0
    origionalNum = num
    if num == 0 or num == 1:
        print("number: "+str(num)+ " is armstrong number")
        return True
    elif num <0:
        print("Negative number")
        return False
    else:
        return calculateArm(num, sumNum, origionalNum)


def calculateArm(num, sumNum, origionalNum):
    while num != 0:
        rnum = num%10
        sumNum = sumNum + rnum**3
        num = num//10
    print(sumNum)
    if (sumNum == origionalNum):
        print("Number is armstrong number")
        return True
    else:
        print("not a armstrong number")
        return False


num = 370
print(armnum(num))
