from string import whitespace, punctuation

all = whitespace + punctuation

#очистка теста от спец.символов
def text_list(text):
    text = text.lower()
    for char in all:
        if char in text:
            text = text.replace(char, " ")
    text = text.split(" ")
    text.sort()
    while text[0] == "":
         text.remove("")
    return text

#создает словать с переводом
def get_vocabluary(fist_text):
    for i in range(0, len(fist_text)):
        result = dict((i, None) for i in fist_text)
    for i in range(0, len(fist_text)):
        if result.get(fist_text[i]) is None:
            result[fist_text[i]] = translate(fist_text[i])
    return result

#перевод слова из текста
def translate(word):
    new_string = ""
    while new_string == "" or new_string in all:
        new_string = (input("Enter translate for '{}':  ".format(word))).lower()
    return new_string


if __name__ == "__main__":
    vocabluary = {}
    text = "Здесь определяется текст на котором будет продемонстрирована правильность работы программы." \
           "Текст должен быть многострочным." \
           "" \
           "В тексте должны быть пустые строки" \
           " и использоваться знаки из whitespace, например +"


    txt = text_list(text)

    vocabluary = get_vocabluary(txt)


    print(" <<<<<<<<<<<<<<<<< DICTIONARY >>>>>>>>>>>>>>>>")
    for key, value in vocabluary.items():
        width = 20
        print("| {} | {} |".format(key.ljust(width), value.ljust(width)))
    print("-" * 47)