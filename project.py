import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

for i in range(1, 5):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url)

    if response.status_code == 200:
        response_content = response.content
        soup = BeautifulSoup(response_content, 'html.parser')
        ol = soup.find('ol')
        articles = ol.find_all('article', class_='product_pod')

        for article in articles:
            image = article.find('img')
            title = image.attrs['alt']
            star = article.find('p', class_='star-rating')
            star = star['class'][1]
            price = article.find('p', class_='price_color').text
            price = float(price[1:])
            books.append([title, price, star])
    else:
        print(f"Failed to retrieve page {i}")
for book in books:
    print(book)
df = pd.DataFrame(books, columns= ['Title', 'Price', 'Star Rating'])
df.to_csv('books.csv')
df