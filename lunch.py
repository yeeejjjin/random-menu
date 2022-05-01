import random

file = open("/Users/joyejin/project/random-menu/data.txt", "r")

strings = file.readlines()
file.close()

print(strings)
print("==========")

menus = []

for s in strings:
    s = s.replace("\n", "")
    print(s)  # 떡볶이,1000,분식

    arr = s.split(",")
    print(arr)  # ['떡볶이', '1000', '분식']
    print(arr[0])
    print(arr[1])
    print(arr[2])

    menus.append({"name": arr[0], "price": arr[1], "category": arr[2]})

print(menus)


print("메뉴:")
for menu in menus:
    print(menu["name"], menu["price"], menu["category"])

i = random.randint(0, len(menus) - 1)
print("\n\n[추천]")
print("- 이름:", menus[i]["name"])
print("- 가격:", menus[i]["price"])
print("- 카테고리:", menus[i]["category"])
