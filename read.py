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
