import json
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

def get_products(file_path):
    with open(file_path) as file:
        src = file.read()

        soup = BeautifulSoup(src, 'html.parser')
        products = soup.find_all('div', class_='product-card')

        urls = []
        product_list = []

        for product in products:
            # Получаем все нужные данные для списка product_list
            product_id = product.get('data-sku')
            product_name = product.find('div', class_='product-card-photo__content').find('a').get('title')
            product_url = 'https://online.metro-cc.ru' + product.find('div', class_='product-card-photo__content').find('a').get('href')
            urls.append(product_url)   # сохраняем ссылки также в отдельном списке, для выгрузки в отдельный файл

            # Достаем актуальную цену из span-ов с рублями и копейками, если все найдено, склеиваем в итоговую цену
            regular_price_rubles = product.find('span', class_='product-card-prices__actual').find('span',
                                                                                                   class_='product-price__sum-rubles')
            regular_price_penny = product.find('span', class_='product-card-prices__actual').find('span',
                                                                                                  class_='product-price__sum-penny')
            if regular_price_rubles is not None:
                regular_price = regular_price_rubles.text.strip()
                if regular_price_penny is not None:
                    regular_price += regular_price_penny.text.strip()
            else:
                regular_price = None

            # Для акционных товаров указана старая цена, находим ее если указана
            promo_price_rubles = product.find('span', class_='product-card-prices__old')
            if promo_price_rubles is not None:
                promo_price = promo_price_rubles.find('span', class_='product-price__sum-rubles').text.strip()
                promo_price_penny = product.find('span', class_='product-card-prices__old').find('span',
                                                                                                 class_='product-price__sum-penny')
                if promo_price_penny is not None:
                    promo_price += promo_price_penny.text.strip()
            else:
                promo_price = None


            # Для брендов заходим на страницу товара
            response = requests.get(url=product_url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            try:
                brand = soup.find('div', class_='product-page-content__attributes-full').find('span', class_='product-attributes__list-item-value').text.strip()
            except Exception as _ex:
                brand = None

            # Собираем все данные по товару в список
            product_list.append({
                "id": product_id,
                "name": product_name,
                "url": product_url,
                "regular_price": regular_price,
                "promo_price": promo_price,
                "brand": brand
            })

        print(len(product_list))

        # with open('items_urls.txt', 'w') as file:
        #     for url in urls:
        #         file.write(f'{url}\n')

        with open('products.json', 'w', encoding='utf-8') as file:
            json.dump(product_list, file, indent=4, ensure_ascii=False)



def main():
    get_products(file_path='result_pars.html')


if __name__ == "__main__":
    main()
