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
        snils, score, accept = td_list[1].text, td_list[4].text, td_list[10].text
        abit.append((snils, score, accept))
    return abit


def accept_rate(full_abit, my_score):
    abit = list(
        filter(lambda x: (x[2] == "Да" and x[1] == '') or (x[2] == "Да" and float(x[1].replace(',', '.')) >= my_score),
               full_abit))
    return abit


table_url = input("url of the competition table: ")
my_score = int(input("your score: "))
result = accept_rate(pars(mk_soup(table_url)),
                     my_score)
print(len(result))
print(*result)
