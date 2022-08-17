
def cook_book():
    with open('cook_book.txt', encoding='utf-8') as f:
        cook_book = {}
        dish = f.readline().strip('\n')
        while dish:
            cook_book[dish] = []
            num = f.readline()

            for i in range(int(num)):
                ing = f.readline().strip('\n').split('|')
                cook_book[dish].append(
                    {'ingredient_name': ing[0].strip(), 'quantity': int(ing[1].strip()), 'measure': ing[2].strip()})

            f.readline()  # skip empty
            dish = f.readline().strip('\n')

    return cook_book
print(cook_book())

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = dict()
    for dish in dishes:
        for ingredients in cook_book[dish]:
            i = dict()
            i['measure'] = ingredients['measure']
            i['quantity'] = ingredients['quantity'] * person_count
            ingredients_list[ingredients['ingredient_name']] = i
    return ingredients_list
print(get_shop_list_by_dishes(dishes=['Утка по-пекински', 'Омлет'], person_count=3))