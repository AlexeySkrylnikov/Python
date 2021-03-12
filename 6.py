number_of_products = int(input('Укажите кол-во товара: '))

product_list = []
product_analytics = {'Название товара': [], 'Цена': [], 'Кол-во': [], 'Еденица': []}

product_dict_copy = {}

number = 0

while number != number_of_products:
    number += 1

    products_list = dict({'Название товара': input(f'Название товара №{number}: '),
                          'Цена': input('Цена: '),
                          'Кол-во': int(input('Укажите кол-во товара: ')),
                          'Еденица': input('Еденица: ')
                          })
    product_list.append((number, products_list))
    for k in products_list.keys():
        product_analytics[k].append(products_list[k])

print('\nСписок продукции: ')
print(product_list)

print('Аналитика: ')
print(product_analytics)
