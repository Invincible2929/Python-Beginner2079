name = "Sushil"
upper_case = name.upper()  # converts name to upper case
print(upper_case)

lower_case = name.lower()  # converts name to lower case
print(lower_case)

no_of_chars = name.count("s")  # count the no. of s in name variable
print(no_of_chars)

total_word_length = len(name)  # cont the word length
print(total_word_length)

nos = [12, 4, 6, 10, -11]
a = sorted(nos)  # sorts the list to ascending order
print(a)

print(name.capitalize())

print(name.isupper())

new = "Srijan"
if new.isupper() == True:  # or if new == new.upper():
    pass
else:
    print(new.upper())

name = "Smith"
if name.count("S") > 0:  # or if name.count("S") > 0:
    print(name.upper())
else:
    pass

txt = "I like banana"
print(txt.replace("banana", "apple"))  # replace any value with given value
print(txt.find("I like"))  # finds the index no. of first finding character
print(txt.index("I like"))  # same as find???????

file = open("e:/s.txt", "r")
text = file.read()
print(text)


# check whether the combination of  word SAMPQE can make a new word SAME or not.
def word_from_let(word, letters):
    Flag = False
    for i in word:
        if i in letters:
            if (word.count(i) <= letters.count(i)):
                Flag = True
            else:
                Flag = False
                break
        else:
            Flag = False
            break
    return Flag


result1 = word_from_let("SAME", "SAMPQE")
print(result1)


# IF EAIONRTLSU:1 DG:2 BCMP:3 FHVWY:4 K:5 JX:8 QZ:10 find the SUM of CREATIVE

# def value(EAIONRTLSU, DG, BCMP, FHVWY, K, JX, QZ):
#     total = 0
#     for i in numbers:
#         if "CREATIVE":
#             total += numbers
#     return total
#
#
# y= value({"1", "2", "3", "4", "5", "8", "10"})
# print(y)

def word_scores(word):
    wordscore = 0
    for i in word:
        if i in "EAIONRTLSU":
            wordscore += 1
        elif i in "DG":
            wordscore += 2
        elif i in "BCMP":
            wordscore += 3
        elif i in "FHVWY":
            wordscore += 4
        elif i in "K":
            wordscore += 5
        elif i in "JX":
            wordscore += 8
        else:
            wordscore += 10
    return wordscore


result = word_scores("CREATIVE")
print(result)


# check if BMOEALMR can create words - LAMB, REAL, WONDER ALSO FIND VALUE LAMB=8, REAL=4
# IF EAIONRTLSU:1 DG:2 BCMP:3 FHVWY:4 K:5 JX:8 QZ:10 find the SUM of CREATIVE

def value(word):
    word_score = 0
    for i in word:
        if i in "EAIONRTLSU":
            word_score += 1
        elif i in "DG":
            word_score += 2
        elif i in "BCMP":
            word_score += 3
        elif i in "FHVWY":
            word_score += 4
        elif i in "K":
            word_score += 5
        elif i in "JX":
            word_score += 8
        else:
            word_score += 10
    return word_score


print(value("ADVENTURES"))


# check if BMOEALMR can create words - LAMB, REAL, WONDER ALSO FIND VALUE LAMB=8, REAL=4


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
