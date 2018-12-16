from string import whitespace, punctuation

all = whitespace + punctuation

#очистка теста от спец.символов
def text_list(text, all):
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

# сортировка словаря по алфавиту перевода (через копирование словаря)
def dict_sort(new_dict):
    list_volues = list(new_dict.values())
    list_keys = list(new_dict.keys())
    new_copy = dict(zip(list_volues, list_keys))
    list_volues.sort()
    for i in range(0, len(list_volues)):
        dict_copy = dict((i, None) for i in list_volues)
    for i in range(0, len(list_volues)):
        dict_copy[list_volues[i]] = new_copy[list_volues[i]]
    list_volues = list(dict_copy.values())
    list_keys = list(dict_copy.keys())
    dict_copy = dict(zip(list_volues, list_keys))
    return dict_copy

# перевод заданого теста с сохранением минимальной пунктуации
def translate_text(text,new_dict):
    point = '.'
    zpt = ','
    text = text.lower()
    for char in point:
        if char in text: text = text.replace(char, " . ")
    for char in zpt:
        if char in text: text = text.replace(char, " , ")
    list_text = text.split()
    new_dict.update([(".", "."), (",", ",")])
    for i in range(0, len(list_text)):
        if list_text[i] in new_dict:
            list_text[i] = new_dict[list_text[i]]
    trantlate_txt = (" ".join(str(x) for x in list_text))
    print("Translate of text :", trantlate_txt)
    return trantlate_txt

if __name__ == "__main__":
    vocabluary = {}
    text = "Здесь определяется текст на котором будет продемонстрирована правильность работы программы." \
           "Текст должен быть многострочным." \
           "" \
           "В тексте должны быть пустые строки" \
           " и использоваться знаки из whitespace, например +"


    txt = text_list(text,all)
    new_dict = get_vocabluary(txt)
    dict_copy = dict_sort(new_dict)

    print(" <<<<<<<<<<<<<<<<< DICTIONARY >>>>>>>>>>>>>>>>")
    for key, value in dict_copy.items():
        width = 20
        print("| {} | {} |".format(key.ljust(width), value.ljust(width)))
    print("-" * 47)
    translate_text(text, new_dict)