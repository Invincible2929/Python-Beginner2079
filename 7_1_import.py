import a

print(a.x)
print(a.y)

from a import x

print(x)

from a import add

add(2, 3)


def find_words(word_list, letters):
    matched = []
    for i in word_list:
        boolean = True
        count = 0
        for x in i:
            if x in letters:
                count += 1
            else:
                count -= 1
        if (count == len(i)):
            matched.append(i)
    return matched


result = find_words(["LAMB", "REAL", "WONDER"], "BMOEALMR")
print(result)
