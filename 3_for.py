
# * Посчитать и вывести суммарное количество продаж для каждого товара
# * Посчитать и вывести среднее количество продаж для каждого товара
# * Посчитать и вывести суммарное количество продаж всех товаров
# * Посчитать и вывести среднее количество продаж всех товаров


products = [
      {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
      {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
      {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

def main(products):
    all_product_sales = 0
    one_product_sales = 0
    all_sales_count = 0
    for item in products:  
        product, items_sold = item.values()
        for sale in items_sold:
            one_product_sales += sale
        print(f'Суммарное количество продаж {product}: {one_product_sales}')
        print(f'Среднее количество продаж {product}: {round(one_product_sales / len(items_sold), 2)}')   
        all_product_sales += one_product_sales
        all_sales_count += len(items_sold)
        one_product_sales = 0
    print(f'Суммарное количество всех продаж: {all_product_sales}')
    print(f'Среднее количество всех продаж: {round(all_product_sales / all_sales_count, 2)}')     

if __name__ == "__main__":
    print(main(products))
