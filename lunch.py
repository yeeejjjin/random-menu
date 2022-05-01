import random

menus = [{
    'name': '김치볶음밥',
    'price': 6000
},
{
    'name': '초밥',
    'price': 10000
},
{
    'name': '라면',
    'price': 6000
}]

l = len(menus) # length: 3
print(l)
print('메뉴:')
for i in range(l): # range(3) -> 0,1,2
    print(i)

    menu = menus[i]
    print(menu['name'], menu['price'])

# print(i)

i = random.randint(0, len(menus) - 1)
print('추천 메뉴:', menus[i]['name'])
print('메뉴 가격:', menus[i]['price'])