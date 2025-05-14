# n = int(input())
# arr = []
# for i in range(n):
#     num = int(input())
#     arr.append(num)

# if n < 2:
#     print("false")
# else:
#     is_fib = True
#     for i in range(2, n):
#         if arr[i] != arr[i-1] + arr[i-2]:
#             is_fib = False
#             break
#     if is_fib:
#         print("true")
#     else:
#         print("false")

# x = 153

# x_str = str(x)
# n = len(x_str)

# sum = 0
# for i in range(n):
#     sum += (int(x_str[i]))**n

# if (sum == x):
#     print("true")
# else:
#     print("false")

# First 50 barrels: 2 gold coin per barrel
# Next 100 barrels: 4 gold coins per barrel
# Next 100 barrels: 6 gold coins per barrel
# More than 250 barrels: 8 gold coins per barrel
# But beware! The tavern keeper is a greedy scallywag—he adds a 50% extra tax on the total amount!

# n = int(input())


# if (n <= 50):
#     rate = 2
#     price = (n*rate)+(0.05*(n*rate))

# elif (n in range(51, 151)):
#     rate = 4
#     price = (n*rate)+(0.05*(n*rate))

# elif (n in range(151, 251)):
#     rate = 6
#     price = (n*rate)+(0.05*(n*rate))

# elif (n > 250):
#     rate = 8
#     price = (n*rate)+(0.05*(n*rate))

# print(price)

# def calculate_cost(n):
#     total_cost = 0
#     if n <= 50:
#         total_cost = n * 2
#     elif n <= 150:
#         total_cost = 50 * 2 + (n - 50) * 4
#     elif n <= 250:
#         total_cost = 50 * 2 + 100 * 4 + (n - 150) * 6
#     else:
#         total_cost = 50 * 2 + 100 * 4 + 100 * 6 + (n - 250) * 8

#     total_cost += total_cost * 0.5

#     return int(total_cost)

# n = int(input())
# print(calculate_cost(n))


# n = int(input())
# temp = n
# bin = ""

# while n > 0:
#     bin = str(n % 2) + bin
#     n = n//2
# print(bin)


# inp = input()
# print(longest_alpha_sequence(inp))

# fib = [3, 2, 3, 5]
# req_fib = fib[1:len(fib)]

# flg = False

# for i in range(len(req_fib)-1, 1, -1):
#     # print(i)
#     print(req_fib[i])
#     if (req_fib[i] == req_fib[i-1]+req_fib[i-2]):
#         flg = True
#         break


# print(flg)
