import math
import time

# def mul(nums):
#     return math.prod(nums)

# l = list(map(int, input().split()))
# d = mul(l)
# print(d)

# def coun(word):
#     up = sum(1 for i in word if i.isupper())
#     lo = sum(1 for i in word if i.islower())
#     return up, lo

# a = input()
# u, l = coun(a)
# print(u, l)

# def p_check(word):
#     f, l = 0, len(word)-1
#     d = list()
#     while f < l:
#         if word[f] == word[l]:
#             d.append(True)
#         else:
#             d.append(False)
#         f += 1
#         l -= 1
#     return d

# s = input()
# a = all(p_check(s))
# print(a)

# def sqrt(num, delay):
#     time.sleep(delay/1000)
#     return math.sqrt(num)

# num = float(input())
# delay = int(input())
# root = sqrt(num, delay)
# print(f"Square root of {num} after {delay} miliseconds is {root}")

def check(x):
    return bool(int(x))

i = input().split()
a = tuple(map(check ,i))
print(all(a))