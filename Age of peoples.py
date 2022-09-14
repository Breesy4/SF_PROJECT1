"""
"Преобразование возраста человека"
def define_age(age):
    months = {
    'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 
    'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8, 
    'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12, 
    }
    split_age = age.split(' ')
    new_age_list = split_age[7:10]
    new_age_list[1] = months[new_age_list[1]]
    return ', '.join(map(str, new_age_list))

hh['Возраст'] = hh['Пол, возраст'].apply(define_age)
hh['Возраст'] = pd.to_datetime(hh['Возраст'])
hh = hh.drop(['Пол, возраст'], axis=1)
display(hh)
"""