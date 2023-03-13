#3.25
word = input() #Hello there
while word !='Done' and word != 'done' and word != 'd':
    new_word = ""
    for letter in reversed(word):
        new_word += letter
    print(new_word)
    word = input()
