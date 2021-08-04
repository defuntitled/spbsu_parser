from bs4 import BeautifulSoup
import requests


def mk_soup(url):
    source = requests.get(
        url).content
    source = source.decode('UTF-8')
    soup = BeautifulSoup(source, 'lxml')
    return soup


def pars(root):
    table = root.find('tbody')
    abit = []
    for tr in table.select('tr'):
        td_list = tr.select('td')
        if not td_list:
            continue
        snils, score = td_list[1], td_list[4]
        abit.append((snils.text, score.text))
    return abit


def accept_rate(root, my_score):
    table = root.find('tbody')
    abit = []
    for tr in table.select('tr'):
        td_list = tr.select('td')
        if not td_list:
            continue
        snils, score = td_list[1], td_list[4]
        if (score.text != ''):
            score = float(score.text.replace(',', '.'))
        else:
            score = 4000
        if td_list[10].text == "Да" and score >= my_score:
            abit.append((snils.text, score))
    return abit


table_url = input("url of the competition table: ")
my_score = int(input("your score: "))
result = accept_rate(mk_soup(table_url),
                     my_score)
print(len(result))
print(*result)
