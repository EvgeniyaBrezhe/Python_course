# Сортировка, регулярные выражения, функциональное программирование?
# my_list = [1, 3, -10, 0, 500, 234]
# my_list.sort()
# НЕ возвращает новый объект, ломаем старый список
# сделать копию или пользоваться другим методом сортировки, который возвращает уже копию
# print(my_list)

# my_list = ['1', '3', '-10', '0', '500', '234', 100, '-30', '3', 'abc', 'cde', '!']
# сортирует строки в алфавитном порядке
# cut_list = [value for value in my_list if type(value) == str]
# new_list = sorted(my_list, reverse=False, key=len)
# fix_list = [str(value) for value in my_list]
# new_list = sorted(cut_list, reverse=False, key=len)
# new_list = sorted(my_list, reverse=False, key=len)

# возвращает новый объект
# key - параметр сортировки, например, длина строки // key=len
# print(new_list)
# print(my_list)

# ФУНКЦИЯ СОРТИРОВКИ
# то, что мы может поставить вместо key, которое будет помогать сортировать

# def sort_key(value):
#     return len(str(value))
#
# my_list = ['1', '3', '-10', '0', '500', '234', 100, '-30', '3', 'abc', 'cde', '!']
# new_list = sorted(my_list, key=sort_key)
# print(new_list)
# возможные проблемы сортировки

# def sort_key(value_dict):
#     return value_dict['name']
#
#
# persons = [{'name': 'John1', 'age': 20},
#            {'name': 'Alma', 'age': 21},
#            {'name': 'Hendrick', 'age': 19}]
#
# new_persons = sorted(persons, key=sort_key)
# print(new_persons)

# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ - выражение, в котором схематическим образом или спец символами мы пытаемся описать
# закономерность в строке
# re - regular expressions, findall
import re


# test_str = 'skdfj(066)-5666666-60-67hsdfjasdfl(067)-524-20-27sdfsdfasdf'
# # reg_exp = r'\([0-9]{3}\)-[0-9]{3}-[0-9]{2}-[0-9]{2}'
# reg_exp = r'[0-9]{2,4}'
# result = re.findall(reg_exp, test_str)
# print(result)

# def sort_list(value_str):
#     date = re.findall(r'[0-9]{1,4}', value_str)
#     if date:
#         date = int(date[0])
#     else:
#         date = 0
#     date = (-1) * date if 'до н.э.' in value_str else date
#     return date
#
# # test_list_1 = []
# test_list = [
#     '1945 - окончание второй мировой войны',
#     '988 - крещение Руси',
#     '1991 - провозглашение независимости Украины',
#     '1073 до н.э. - за тысячу лет до восстания Спартака'
# ]
#
# new_list = sorted(test_list, key=sort_list)
# print(new_list)


albert = '''Physics, philosophy
Institutions	
Swiss Patent Office (Bern) (1902–1909)
Swiss Patent Office (Bern) (1902–1909)Swiss Patent Office (Bern) (1902–1909)Swiss Patent Office (Bern) (1902–1909)
Swiss Patent Office (Bern) (1902–1909)Swiss Patent Office (Bern) (1902–1909)Swiss Patent Office (Bern) (1902–1909)Swiss Patent Office (Bern) (1902–1909)Swiss Patent Office (Bern) (1902–1909)

University of Bern (1908–1909)
University of Zurich (1909–1911)
Charles University in Prague (1911–1912)
ETH Zurich (1912–1914)
Prussian Academy of Sciences (1914–1933)
Humboldt University of Berlin (1914–1933)
Kaiser Wilhelm Institute (director, 1917–1933)
German Physical Society (president, 1916–1918)
Leiden University (visits, 1920)
Institute for Advanced Study (1933–1955)
Caltech (visits, 1931–1933)
University of Oxford (visits, 1931–1933)
Barnard Medal (1920)
Nobel Prize in Physics (1921)
Matteucci Medal (1921)
ForMemRS (1921)[3]
Copley Medal (1925)[3]
Gold Medal of the Royal Astronomical Society (1926)
Max Planck Medal (1929)
Member of the National Academy of Sciences (1942)
Time Person of the Century (1999)
В 1931 году Эйнштейн снова побывал в США. В Пасадене его очень тепло встретил Майкельсон, которому оставалось жить четыре месяца. Вернувшись летом в Берлин, Эйнштейн в выступлении перед Физическим обществом почтил память замечательного экспериментатора, заложившего первый камень фундамента теории относительности.
В ходе и после Первой мировой войны в результате развития антисемитских настроений теории Эйнштейна подвергались постоянным нападкам. Была создана антиэйнштейновская организация. Известно об осуждении одного человека за подстрекательство к убийству Эйнштейна с назначенным штрафом в шесть долларов. Одним из результатов кампании против учёного явилось издание в 1931 году книги «Сто авторов против Эйнштейна»[46], на которое Эйнштейн ответил «Будь я не прав, хватило бы и одного!»[47]. Примерно до 1926 года Эйнштейн работал в очень многих областях физики, от космологических моделей до исследования причин речных извилин. Далее он, за редким исключением, сосредотачивает усилия на квантовых проблемах и Единой теории поля.'''

reg_exp = r'[0-9]{4}'
results = re.findall(reg_exp, albert)
new_results = sorted(results, key=albert.count)
print(new_results)