# 10926
# name = input()
# print(name + "??!")

# 18108
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
# num = int(input())
# str = ""
# for i in range(num//4):
#     str += "long "
# print(str+"int")

# 11021
# a = int(input())
# for i in range(a):
#     b,c = map(int,input().split())
#     print(f"Case #{i+1}: {b+c}")

# 11022
# a = int(input())
# for i in range(a):
#     b,c = map(int,input().split())
#     print(f"Case #{i+1}: {b} + {c} = {b+c}")

# 2438
# a = int(input())
# for i in range(a):
#     print("*"*(i+1))

# 2439
# a = int(input())
# for i in range(a):
#     print(" "*(a-i-1) + "*"*(i+1))

# 10952
# while True:
#     a,b = map(int,input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)

# 10807
# a = int(input())
# b = list(map(int,input().split()))
# find = int(input())
# print(b.count(find))

# 10871
# a,b = map(int, input().split())
# c = list(map(int,input().split()))
# for i in c:
#     if b > i:
#        print(i, end=" ")

# 10818
# a = int(input())
# b = list(map(int,input().split()))
# print(min(b),max(b))

# 2562
# a = []
# for i in range(9):
#     a.append(int(input()))
# print(max(a))
# print(a.index(max(a)) + 1)

# 10810
# a,b = map(int,input().split())
# pack = [0] * a
# for i in range(b):
#     c,d,e = map(int,input().split())
#     for j in range(c-1,d):
#         pack[j] = e
# print(*pack)

# 10811
# a,b = map(int,input().split())
# lst = [i+1 for i in range(a)]
# for i in range(b):
#     c,d = map(int,input().split())
#     lst[c-1:d] = lst[c-1:d][::-1]
# print(*lst)
# lst = ' '.join(map(str,lst))
# print(lst)

# 10813
# a,b = map(int,input().split())
# lst = [i+1 for i in range(a)]
# for i in range(b):
#     c,d = map(int,input().split())
#     temp = lst[c-1]
#     lst[c-1] = lst[d-1]
#     lst[d-1] = temp
# print(*lst)


# 5597
# a = [0]*28
# b = []
# for i in range(28):
#     a.append(int(input()))
# for j in range(1,31):
#     if a.count(j) == 0:
#         b.append(j)
# b.sort()
# print(b[0])
# print(b[1])

# 3052
# a, b = [], []
# count = 0
# for i in range(10):
#     a.append(int(input()))
# for j in a:
#     b.append(j % 42)
# for k in range(42):
#     if b.count(k) >= 1:
#         count += 1
# print(count)

# 1546
# average = 0.0
# count = int(input())
# lst = list(map(int,input().split()))
# d = max(lst)
# for i in lst:
#     average += i / d * 100
# print(average/len(lst))
# for 문 대신 sum을 사용하기
# average = sum((i / d) * 100 for i in lst) / len(lst)
# print(average)


# 27866
# str = input()
# idx = int(input())
# print(str[idx-1])

# 2743
# str = input()
# print(len(str))

# 9086
# loop = int(input())
# for i in range(loop):
#     str = input()
#     print(str[0]+str[-1])

# 11720
# num = int(input())
# nums = input()
# count = 0
# for i in range(len(nums)):
#     count += int(nums[i])
# print(count)

# 10809
str = input()
lst = [0] * 28

