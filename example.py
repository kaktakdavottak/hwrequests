import requests
import os

API_KEY = 'trnsl.1.1.20181202T140718Z.a5b5308460109d94.1a44b33df20a5dbfef7c99185fc1ebfd747fd275'
URL_TRANSLATE = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
URL_DETECT = 'https://translate.yandex.net/api/v1.5/tr.json/detect'


def translate_it(text, from_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-ru'.format(from_lang),
    }

    response = requests.get(URL_TRANSLATE, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


def detect_lang_it(text):
    """
    https://translate.yandex.net/api/v1.5/tr.json/detect
    ? [key=<API-ключ>]
    & text=<текст>
    & [hint=<список вероятных языков текста>]
    & [callback=<имя callback-функции>]
    """

    params = {
        'key': API_KEY,
        'text': text,
    }

    response = requests.get(URL_DETECT, params=params)
    json_ = response.json()
    return ''.join(json_['lang'])


def get_file_list():
    file_format = '.txt'
    list_file = []
    for txt_file in os.listdir():
        if file_format in txt_file:
            list_file.append(txt_file)
    return list_file


def translate_file():
    for file in get_file_list():
        with open(file, encoding='utf-8') as f:
            init_text = f.read()
            with open((file.split('.')[0] + '_ru.txt'), 'w', encoding='utf-8') as wf:
                wf.write(translate_it(init_text, detect_lang_it(init_text))
                         + '\n Переведено сервисом «Яндекс.Переводчик» \n http://translate.yandex.ru/')
    return


if __name__ == "__main__":
    translate_file()
