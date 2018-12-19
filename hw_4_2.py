from string import ascii_letters
from hw_4_1 import clear_word

filterstr = ascii_letters + " "
#отбирает англ символы и пробелы (что бы слова можно было отделить)
def get_eng_words(text):
    eng = []
    text = list(text.lower())
    for i in range(0, len(text)):
        if text[i] in filterstr:
            eng.append(text[i])
    result = ("".join(str(x) for x in eng))
    result = result.split(" ")
    result.sort()
    while result[0] == "":
        result.remove("")
    return result


if __name__ == "__main__":
    text = "Объявившим голодовку сотрудникам хлебокомбината начали выплачивать задолженность по зарплате, говорится в сообщении на сайте прокураты Москвы." \
           "The Commission had demanded changes to Italy's budget plans because of the country's high debt."
    try:
        text = clear_word(text, filterstr)
    except ValueError:
        eng_word = set(get_eng_words(text))
        print(eng_word)