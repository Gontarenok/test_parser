import json

from bs4 import BeautifulSoup

def get_urls(file_path):
    with open(file_path) as file:
        src = file.read()

        soup = BeautifulSoup(src, 'html.parser')
        products = soup.find_all('div', class_='product-card')
        print(len(products))
        urls = []
        product_list = []
        for product in products:
            # product_img = item.find('div', class_='product-card-photo__content').find('img').get('src')
            product_id = product.get('data-sku')
            product_name = product.find('div', class_='product-card-photo__content').find('a').get('title')
            product_url = 'https://online.metro-cc.ru' + product.find('div', class_='product-card-photo__content').find('a').get('href')

            # Достаем актуальную цену из span-ов с рублями и копейками, если все найдено, склеиваем в итоговую цену
            regular_price_rubles = product.find('span', class_='product-card-prices__actual').find('span', class_='product-price__sum-rubles')
            regular_price_penny = product.find('span', class_='product-card-prices__actual').find('span', class_='product-price__sum-penny')
            if regular_price_rubles is not None:
                regular_price = regular_price_rubles.text
                if regular_price_penny is not None:
                    regular_price += regular_price_penny.text
            else:
                regular_price = None

            # Для акционных товаров указана старая цена, находим ее если указана
            promo_price_rubles = product.find('span', class_='product-card-prices__old')
            if promo_price_rubles is not None:
                promo_price = promo_price_rubles.find('span', class_='product-price__sum-rubles').text
                promo_price_penny = product.find('span', class_='product-card-prices__old').find('span', class_='product-price__sum-penny')
                if promo_price_penny is not None:
                    promo_price += promo_price_penny.text
            else:
                promo_price = None

            # brand =

            # item_url = item.find('a', class_='product-card-name'.find('span')).text
            product_list.append(promo_price)


            # product_list.append({
            #     "id": product_id,
            #     "name": product_name,
            #     "url": product_url,
            #     "regular_price": regular_price,
            #     "promo_price": promo_price,
            #     "brand": brand
            # })
        print(product_list)
        print(len(product_list))

        # with open('items_urls.txt', 'w') as file:
        #     for url in urls:
        #         file.write(f'{url}\n')

        # with open('products.json', 'w') as file:
        #     json.dump(product_list, file, indent=4)


get_urls(file_path='result_pars.html')
