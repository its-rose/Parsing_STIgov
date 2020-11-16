import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.sti.gov.kg/'

def get_html():
    response = requests.get(url)
    return response.text

# https://www.sti.gov.kg/allnews
# https://www.sti.gov.kg/allnews/page/59
all_pages = []
pagination = 'allnews/page/'
def get_all_pages():
    for page in range(0, 59):
        page += 1
        page_url = f'{url}{pagination}{page}'
        all_pages.append(page_url)
        with open('all_pages.txt', 'w') as file:
            for i in all_pages:
                file.write(f'{i}\n')
get_all_pages()

# /html/body/form/div[6]/div/div/div[2]/div/div[2]/div[1]/div/ul/li[1]/h2/a
# /html/body/form/div[6]/div/div/div[2]/div/div[2]/div[1]/div/ul/li[5]/h2/a
# /html/body/form/div[6]/div/div/div[2]/div/div[2]/div[2]/div/ul/li[1]/h2/a
# /html/body/form/div[5]/div/div/div[2]/div/div/div/div/ul/li[2]/a

all_news = []
html = get_html()
soup = BS(html, 'html.parser')
def get_all_news():
    h2 = soup.find('body').find_all('h2')
    for news1 in h2:
        try:
                a = news1.find('a').get('href')
                a = f'{url}{pagination}{a}'
                all_news.append(a)
                print(a)
        except Exception as ex:
            pass
    with open('all_news.txt', 'w') as file:
        for news1 in all_news:
            file.write(f'{news1}\n')
get_all_news()