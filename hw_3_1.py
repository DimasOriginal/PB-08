from string import punctuation, whitespace

all = whitespace + punctuation

def enter_text(all):
    new_string = " "
    all_list = [" "]
    all = whitespace + punctuation
    while new_string != [""]:

            new_string = (input("Enter string: ")).lower()

            for sign in all:
                new_string = new_string.replace(sign, " ")
            new_string = new_string.split(" ")
            all_list = all_list + new_string
    return all_list



word = enter_text(all)

while word[0] == "":
    word.remove("")
word.remove(" ")
len_word = len(word)
if len_word != 0:
    rezult = 1
    for i in range(0, len_word - 1):
        if word[i] == word[i + 1]:
            rezult += 1
            continue
        if word[i] != word[i + 1]:
            print("{}  - {}".format(word[i], rezult))
            rezult = 1
    if len_word < 2:
        print("{}  - {}".format(word[0], 1))
    elif word[-1] != word[-2]:
        print("{}  - {}".format(word[-1], 1))
    elif word[-1] == word[-2]:
        print("{}  - {}".format(word[-1], rezult))