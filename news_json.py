import json
from collections import Counter


def top():
    with open("newsafr.json", encoding="utf-8") as f:
        json_data = json.load(f)

    descriptions = json_data["rss"]["channel"]["items"]

    list_of_descriptions = []  # список для слов, в которых больше 6 букв

    for description in descriptions:
        news = description["description"].split()
        for word in news:
            if len(word) > 6:
                list_of_descriptions.append(word)

    top = Counter(list_of_descriptions)
    # print(top.most_common(10))
    print("Топ 10 самых часто встречающихся в новостях слов длиннее"
          " 6 символов:")
    for num_, word_count in enumerate(top.most_common(10), 1):
        # Возвращаем список из 10 наиболее распространенных слов
        # и их количество от наиболее к наименее распространенным
        print(f'{str(num_)} - {word_count[0]} ({word_count[1]} слов)')


while True:
    user_input = input('Введите название файла: ')
    if user_input == 'newsafr.json':
        top()
        break
    else:
        print('Файл не найден.\n')
