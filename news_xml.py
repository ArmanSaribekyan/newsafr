from collections import Counter
import xml.etree.ElementTree as Et


def top():
    parser = Et.XMLParser(encoding="utf-8")
    tree = Et.parse("newsafr.xml", parser)
    root = tree.getroot()

    items = root.findall("channel/item")

    list_of_descriptions = []  # список для слов, в которых больше 6 букв

    for item in items:
        news = item.find("description").text.split()  # разбивает строку на части
        for word in news:
            if len(word) > 6:  # отсекаем слова длинее 6 символов
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
    if user_input == 'newsafr.xml':
        top()
        break
    else:
        print('Файл не найден.\n')

