from bs4 import BeautifulSoup

def get_urls(file_path):
    with open(file_path) as file:
        src = file.read()

        soup = BeautifulSoup(src, 'html.parser')
        items_divs = soup.find_all('div', class_='product-card-photo catalog-2-level-product-card__photo style--catalog-2-level-product-card')

        urls = []
        name = []
        for item in items_divs:
            # item_url_img = item.find('div', class_='product-card-photo__content').find('img').get('src')
            item_url = item.find('div', class_='product-card-photo__content').find('a').get('href')
            urls.append('https://online.metro-cc.ru'+ item_url)
            # item_url = item.find('a', class_='product-card-name'.find('span')).text
            # name.append(item_url)
            # print(name)

        print(len(urls))

        with open('items_urls.txt', 'w') as file:
            for url in urls:
                file.write(f'{url}\n')


get_urls(file_path='result_pars.html')
