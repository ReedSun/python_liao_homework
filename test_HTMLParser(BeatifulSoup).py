import requests
from bs4 import BeautifulSoup


def test():
    resp = requests.get('https://www.python.org/events/python-events/')
    soup = BeautifulSoup(resp.text, 'html.parser')
    new_soup = soup.select_one(".shrubbery")
    for li in new_soup.select('.list-recent-events > li'):
        # BeautifulSoup.select()是一个css选择器,会返回一个列表[]  这其中，
        # 点.表示通过类名查找，
        # 大于号>表示找到某个tag标签（大于号之前）下的直接子标签（大于号之后）
        print('title:', li.find('a').text)
        # BeautifulSoup.find()表示寻找指定的tag
        # BeautifulSoup.text()表示输出文字内容
        print('time:', li.find('time').text)
        print('location:', li.select_one('.event-location').text)
        # BeautifulSoup.select_one()表示将不会返回一个列表[]，继续返回一个BeautifulSoup
        # 不能再继续用find()方法的原因是没有合适的标签了
        print('*' * 100)

if __name__ == "__main__":
    test()
