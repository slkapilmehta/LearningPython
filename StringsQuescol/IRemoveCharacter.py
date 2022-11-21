def remChar(words):
    newWords = ""
    for word in words:
        if word == enteredWord:
            pass
        else:
            newWords = newWords + word
    return (newWords)

enteredWord = input("enter the word: ")
words = "write a program to remove a character/ space from the string"
print(remChar(words))
