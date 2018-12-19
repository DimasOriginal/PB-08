from string import punctuation, ascii_letters, digits

#пробелы не учитывал, при каждом пробеле тода бы выдавало ошибку
filterstr = punctuation + digits

#проверяет на наличие не английских символов
def clear_word(word, filterstr):
    word = list(word)
    for i in range(0, len(word)):
        if word[i] in filterstr:
            if word[i] not in ascii_letters:
                raise ValueError
    return word
#отбирает не английские символы и их позицию в тексте
def clear_world(word):
    id_char = list()
    input_char = list()
    word = list(word)
    for i in range(0, len(word)):
        if word[i] not in ascii_letters:
            input_char.append(word[i])
            id_char.append(i)
    return input_char, id_char

try:

    if __name__ == "__main__":
        word = """Если в слове есть символ не английского алфавита,
            то необходимо вызвать исключение ValueError
            и в сообщении передать сам неверный символ и его позицию.

        :param word: строка
        :param filter: строка из символов, которые надо убрать из строки, переданной в параметре word
        :return: result - строка из параметра word, очищенная от символов, содержащихся в параметре filterstr"""


        clear_word(word, filterstr)
except ValueError:
    print("Its not English")
    input_char, id_char = clear_world(word)
    for i in range (1, len(id_char) - 1):
        print("Incorect char: '{}'    pozition: {}".format(input_char[i], id_char[i]))
