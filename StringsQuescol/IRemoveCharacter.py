def remChar(words):
    newWords = ""
    if enteredWord not in words:
        print("character not present, nothing to remove from:- ")
        return words
    else:
        for word in words:
            if word == enteredWord:
                pass
            else:
                newWords = newWords + word
        return (newWords)

enteredWord = input("enter the character: ")
words = "write a program to remove a character/ space from the string"
print(remChar(words))