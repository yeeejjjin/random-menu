import random

menus = [
    {"name": "김치볶음밥", "price": 6000, "category": "한식"},
    {"name": "초밥", "price": 10000, "category": "일식"},
    {"name": "라면", "price": 6000, "category": "분식"},
    {"name": "햄버거", "price": 5500, "category": "양식"},
    {"name": "샌드위치", "price": 6700, "category": "양식"},
    {"name": "카레", "price": 6500, "category": "일식"},
    {"name": "쌀국수", "price": 7300, "category": "아시안"},
    {"name": "돈까스", "price": 8000, "category": "일식"},
    {"name": "국밥", "price": 5000, "category": "한식"},
    {"name": "떡볶이", "price": 3500, "category": "분식"},
]

l = len(menus)  # length: 3
print(l)
print("메뉴:")
for i in range(l):  # range(3) -> 0,1,2
    print(i)

    menu = menus[i]
    print(menu["name"], menu["price"], menu["category"])

# print(i)

i = random.randint(0, len(menus) - 1)
print("추천 메뉴:", menus[i]["name"])
print("메뉴 가격:", menus[i]["price"])
