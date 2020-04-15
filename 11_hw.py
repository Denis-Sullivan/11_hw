import requests
import json
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

def open_file(file):
    text = ''
    with open(file, encoding='utf-8') as file:
        for line in file:
            text += line
    return text

def write_file(file, text):
    with open(file, 'wt', encoding='utf-8') as file:
        file.write(text)

def translate_it(from_file, to_file, from_lang, to_lang='ru'):
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
    API_KEY = 'trnsl.1.1.20200415T093657Z.a1fc5f43549ff5c8.0e4fb2642473f7b294762de0c8a9f0425d53e88f'
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

    from_text = open_file(from_file)
    params = {
        'key': API_KEY,
        'text': from_text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    write_file(to_file, ''.join(json_['text']))
    print(f'Файл {from_file}, направление перевода: '
          f'{from_lang.upper()}-{to_lang.upper()}. \n '
          f'Файл: {to_file}. Перевод завершён.\n')
# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    # print(translate_it('привет', 'en'))
    translate_it('DE.txt', 'DE_RU.txt', 'de')
    translate_it('ES.txt', 'ES_RU.txt', 'es')
    translate_it('FR.txt', 'FR_RU.txt', 'fr')

