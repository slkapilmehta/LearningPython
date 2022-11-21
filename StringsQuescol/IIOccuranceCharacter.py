def occurCharacter(words):
    count = 0
    for word in words:
        if word == charToCount:
            count += 1
    return count

charToCount = input("enter a character whose occurance has to be counted: ")
words = "program to count occurance of characters 123456 789"
print(occurCharacter(words))