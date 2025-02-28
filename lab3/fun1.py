from itertools import permutations 
import math
import random

# #1.Grams to Ounces
# def grams_to_ounces(grams):
#     return 28.3495231 * grams

# grams =  float(input("Enter weight in grams: "))
# ounces = grams_to_ounces(grams)
# print(ounces)

# #2.Farenheit to Celcius
# def farenheit_to_celcius(F):
#     return (5 / 9) * (F - 32)


# F = float(input("Enter temperature in farenheit: "))
# C = farenheit_to_celcius(F)
# print(C)

# #3.puzzle
# def solve(heads, legs):
#     for ch in range(heads):
#         ra = heads - ch
#         if 2*ch + 4*ra == legs:
#             return ch, ra
#     return None

# heads, legs = int(input("How many heads: ")), int(input("How many legs: "))
# result = solve(heads, legs)
# print(type(result))
# if result:
#     ch, ra = result
#     print(f"{ch} chickens and {ra} rabits")
# else:
#     print("No solution!")

# #4.Prime
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def filter_prime(l):
#     return [int(num) for num in l if is_prime(int(num))]

# #5.permutation
# def per(s):
#     p = permutations(s)
#     for k in p:
#         print("".join(k))
    

# l = input("Enter a word: ")
# per(l)

# l = input()
# k = ["".join(d) for d in permutations(l)]
# print(k)

# #6.reverse
# def reverse_sentence(sentence):
#     words = sentence.split()
#     reversed_words = words[::-1] 
#     return " ".join(reversed_words) 

# user_input = input("Enter a sentence: ")
# print(reverse_sentence(user_input))

# #7.333
# def has_33(nums):
#     for i in range(len(nums) - 1):
#         if nums[i] == 3 and nums[i + 1] == 3:
#             return True
#     return False

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3])) 
# print(has_33([3, 1, 3]))  

# #8.spy
# def spy_game(nums):
#     sequence = [0, 0, 7]
#     index = 0
    
#     for num in nums:
#         if num == sequence[index]:
#             index += 1
#         if index == len(sequence):
#             return True
    
#     return False

# print(spy_game([1, 2, 4, 0, 0, 7, 5])) 
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))  

# #9.sphere
# def sphere_volume(radius):
#     return (4/3) * math.pi * radius**3

# r = float(input("Enter the radius of the sphere: "))
# print(f"Volume of the sphere: {sphere_volume(r)}")

#10.numbers
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

user_input = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in user_input]

print("Unique elements:", unique_elements(numbers))

# #11.pali
# def is_palindrome(s):
#     cleaned = "".join(s.lower().split())  
#     return cleaned == cleaned[::-1]

# user_input = input("Enter a word or phrase: ")
# print("Palindrome" if is_palindrome(user_input) else "Not a palindrome")

# #12.his
# def histogram(lst):
#     for num in lst:
#         print('*' * num)

# user_input = input("Enter numbers separated by spaces: ").split()
# numbers = [int(num) for num in user_input]

# histogram(numbers)

# №13.guess
# def guess_number_game():
#     print("Hello! What is your name?")
#     name = input()

#     number_to_guess = random.randint(1, 20)
#     print(f"Well, {name}, I am thinking of a number between 1 and 20.")

#     attempts = 0
#     while True:
#         print("Take a guess.")
#         guess = int(input())
#         attempts += 1

#         if guess < number_to_guess:
#             print("Your guess is too low.")
#         elif guess > number_to_guess:
#             print("Your guess is too high.")
#         else:
#             print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
#             break

# guess_number_game()
