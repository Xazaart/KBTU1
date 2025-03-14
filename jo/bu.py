import re, json

# with open("lll.txt", "r", encoding="utf-8") as f:
#     data = f.readlines()  # Читаем весь файл как строку

# for i in data:
#     print(i.strip())

# match = re.search(r'\d+', "Цена 100 рублей")
# print(match.group())  # 100

# x = {
#     "aaa": "aasa",
#     "ddd": "aa;a",
#     "1121": "asa"
# }

# y = json.dumps(x, indent=2)
# print(y)




# test = ['ab', 'ba', 'ababab', 'abbbb', 'baaaa', 'aaaab']
# l = r'ab*'
# for q in test:
#     if re.fullmatch(l, q):
#         print(q)

test = ['abb', 'ba', 'ababab', 'abbbb', 'baaaa', 'aaaab']
l = r'ab{2,3}'
for q in test:
    if re.fullmatch(l, q):
        print(q)