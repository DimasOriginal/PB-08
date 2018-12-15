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
    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1]:
            continue
        else:
            print(word[i], end=" ")
    print(word[-1])