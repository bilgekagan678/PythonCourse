import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

news_data = []
for item in soup.select('span.titleline'):
    title = item.a.text
    link = item.a['href']
    news_data.append({'title': title, 'link': link})

for idx, news_item in enumerate(news_data, start=1):
    with open('hackerNewsTop30.txt', 'a' ) as file:
        file.write(f"{idx}. {news_item['title']} || News link: {news_item['link']}\n")

    # This print function is for checking the correctness
    print(f"{idx}. {news_item['title']} || News link: {news_item['link']}")
