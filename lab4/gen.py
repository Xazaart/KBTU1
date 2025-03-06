# def square_gen(N):
#     for i in range(N + 1):
#         yield i ** 2

# N = int(input("Enter N: "))
# for num in square_gen(N):
#     print(num)

# def even_gen(n):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i

# n = int(input("Enter n: "))
# print(','.join(str(i) for i in even_gen(n)))

# def divisible_gen(n):
#     for i in range(n + 1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i

# n = int(input("Enter n: "))
# for num in divisible_gen(n):
#     print(num)

# def squares(a, b):
#     for i in range(a, b + 1):
#         yield i ** 2

# a = int(input("Enter start (a): "))
# b = int(input("Enter end (b): "))
# for value in squares(a, b):
#     print(value)

# def countdown(n):
#     while n >= 0:
#         yield n
#         n -= 1

# n = int(input("Enter n: "))
# for num in countdown(n):
#     print(num)
