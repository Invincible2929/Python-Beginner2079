x = 20
y = 10


def add(x, y):
    print(x + y)


def new_word(word, letter):
    flag = False
    for i in word:
        if i in letter:
            if (word.count(i) <= letter.count(i)):
                flag = True
            else:
                flag = False
                break
        else:
            flag = False
            break
    return flag


y = new_word("SAME", "SAMPQE")
print(y)
