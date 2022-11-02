def get_count_char(str_):  # TODO посчитать количество каждой буквы в строке в аргументе str_
    dict_ = {
    }
    for a in str_.lower():
        if a.isalpha():
            if a in dict_:
                dict_[a] += 1
            else:
                dict_[a] = 1
    return dict_

def get_percent_char(dict_):
    dict_percent = {
    }
    for b in dict_:
        if b in dict_percent:
            dict_percent[b] = dict_.get(b) // sum(dict_.values()) * 100
    return dict_percent
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
