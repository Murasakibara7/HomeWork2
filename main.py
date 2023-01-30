import pprint

with open(r'C:\Users\Vyacheslav\PycharmProjects\HomeWork2\py-homework-basic-files\2.4.files\recipes.txt', 'rt',
          encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        name_of_the_dish = line.strip()
        the_number_of_ingredients_in_the_dish = int(f.readline())
        ingredients = []
        for i in range(the_number_of_ingredients_in_the_dish):
            emp = f.readline().strip()
            ingredient_name, quantity, measure = emp.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure

            })
        f.readline()
        cook_book[name_of_the_dish] = ingredients


    def get_shop_list_by_dishes(dishes, person_count):
        ingredient = {}
        for dish in dishes:
            for k in cook_book[dish]:
                j = k['ingredient_name']
                ingredient[j] = {'measure': k['measure'], 'quantity': int(k['quantity']) * person_count}


    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)




text_dict = {}
with open('1.txt', 'rt', encoding='utf-8') as f1, open('2.txt', 'rt', encoding='utf-8') as f2, open('3.txt', 'rt', encoding='utf-8') as f3:
    res_1 = sum(1 for line in open('1.txt', 'r', encoding='utf-8'))
    res_2 = sum(1 for line in open('2.txt', 'r', encoding='utf-8'))
    res_3 = sum(1 for line in open('3.txt', 'r', encoding='utf-8'))
    st = ['1.txt', '2.txt', '3.txt']
    for i in st:
        with open(f'{i}', encoding='utf-8') as q1:
            name = q1.name
            summ = sum(1 for line in open(f'{i}', 'r', encoding='utf-8'))
            text_dict[name] = summ
    tr = sorted(text_dict.items(), key=lambda x: x[1])
for k in tr:
    file_name = k[0]
    row = k[1]
    with open('result.txt', 'a', encoding='utf-8') as t1:
        t1.write(file_name + '\n')
        t1.write(str(row) + '\n')
        with open(f'{k[0]}', 'rt', encoding='utf-8') as y:
            text = y.readlines()
            t1.write(''.join(text) + '\n')
