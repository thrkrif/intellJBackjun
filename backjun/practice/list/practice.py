# input() 의 반환값? Str
# inp = input()
# print(inp)
# print(type(inp))

# input().split()의 반환값? list, 리스트 내부의 각 요소들의 타입은 str
# ipsplit = input().split()
# print(ipsplit)
# print(type(ipsplit))

# join 함수는 리스트 -> str으로 반환해줌
# ip = ''.join(input().split())
# print(ip)
# print(type(ip))

# 리스트 더하기
lst1 = [1,2,3]
lst2 = 5
# lst3 = list(lst2) -> list(정수) 는 불가능 list(반복 가능한 객체만 들어올 수 있음)
print(lst1+[lst2])