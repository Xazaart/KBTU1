import re
#1 task
# check = r'ab*'
# test_strings=["ab", "aaa", "baa", "abb", "cableee", "babb"]
# for string in test_strings:
#     if re.fullmatch(check, string):
#         print(f"'{string}': True")
#     else:
#         print(f"'{string}': False")

#2 task
# check = r'ab{2,3}'
# s = ["abb", "abbb", "abbbb", "ab", "abbbbbbbb"]
# for st in s:
#     if re.fullmatch(check, st):
#         print({st})

#3 task
# txt = ["qa_lam", "mash", "tashaq", "m_al", "cho_tam"]
# pattern = r'[a-z]+(?:_)+[a-z]*'
# for i in txt:
#     if re.findall(pattern, i):
#         print(i)

#4 task
# txt = ["Qwer", "ygeeg", "Wrtfy", "jkhH", "Yuiop"]
# p = r'^[A-Z]+[a-z]+$'
# for i in txt:
#     if re.findall(p, i):
#         print(i)

#5 task
# q = input()
# l = q.split()
# c = r'b$'
# for i in l:
#     if re.findall(c, i):
#         print("a"+i)


#6 task
# txt = input("Введите строку: ")
# new = txt.replace(" ", ":").replace(",", ":").replace(".", ":")
# print(new)

#7 task
# s = input()
# w = s.split('_')
# print(w[0] + ''.join(word.capitalize() for word in w[1:]))


#8 task
# txt = "QewrrtyYuioOkjG"
# print(re.split(r'(?=[A-Z])', txt))

#9 task
# txt = input()
# new_txt = re.sub(r'(?=[A-Z])', ' ', txt)
# print(new_txt)

#10 task
# txt = input()
# q = (re.sub(r'(?=[A-Z])', '_', txt))
# w = q.lower()
# print(w.replace('_', '', 1))