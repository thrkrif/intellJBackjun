# 10926
# name = input()
# print(name + "??!")

#18108
# year = int(input())
# print(year-543)

# 10403
# A,B,C = map(int,input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

# 2588
# a = int(input())
# b = input()
# print(a*int(b[2]))
# print(a*int(b[1]))
# print(a*int(b[0]))
# print(a*int(b))

# 11382
# a,b,c = map(int,input().split())
# print(a+b+c)

# 10171
# print("\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \(__)|")

# 10172
# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"`    |')
# print("||_/=\\\\__|")

# 9498
# score = int(input())
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# 2753
# year = int(input())
# if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
#     print(1)
# else:
#     print(0)

# 14681
# a = int(input())
# b = int(input())
# if a > 0 and b > 0:
#     print(1)
# elif a < 0 and b > 0:
#     print(2)
# elif a < 0 and b < 0:
#     print(3)
# elif a > 0 and b < 0:
#     print(4)

# 2884
# a,b = map(int,input().split())
# if b >= 45 :
#     print(a, b-45)
# else:
#     if a == 0:
#         print(23, b-45+60)
#     else:
#         print(a-1, b-45+60)

# 2525
# a,b = map(int,input().split())
# c = int(input())
# b += c
# if b >=60:
#     a += b//60
#     b %= 60
# if a >= 24:
#     a %= 24
# print(a,b)

# 2480
# a, b, c = map(int, input().split())
#
# if a == b == c:
#     print(10000+a*1000)
# elif a == b:
#     print(1000+a*100)
# elif a == c:
#     print(1000+a*100)
# elif b == c:
#     print(1000+b*100)
# else:
#     print(100 * max(a,b,c))

# 2739
# a = int(input())
# for i in range(1,10):
#     print(f"{a} * {i} = {a*i}")

# 10590
# num = int(input())
# for i in range(num):
#     a,b = map(int,input().split())
#     print(a+b)

# 8393
# num = int(input())
# count = 0
# for i in range(1,num+1):
#     count += i
# print(count)

# 25304
# prices = int(input())
# nums = int(input())
# score = 0
# for i in range(nums):
#     price,num = map(int, input().split())
#     score += price*num
# print("Yes") if prices == score else print("No")

# 25314
num = int(input())
str = ""
for i in range(num):
    str += "long "
print(str+"int")