
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