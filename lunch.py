import random

menus = [{
    'name': '김치볶음밥',
    'price': 6000,
},
{
    'name': '초밥',
    'price': 10000
},
{
    'name': '라면',
    'price': 6000
},
{
    'name': '햄버거',
    'price': 5500
},
{
    'name': '샌드위치',
    'price': 6700
},
{
    'name': '카레',
    'price': 6500
},
{
    'name': '쌀국수',
    'price': 7300
},
{
    'name': '돈까스',
    'price': 8000
},
{
    'name': '국밥',
    'price': 5000
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