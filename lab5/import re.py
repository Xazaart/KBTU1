import re 

a = r'ab*'
d = ["a", "ab", "abb", "bbb", "aa", "", "aabb", "abbb", "abbbb"]
for l in d:
    if re.fullmatch(a, l):
        print(l)
