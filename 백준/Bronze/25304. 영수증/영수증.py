X = int(input())   # 총 금액
N = int(input())   # 물건 종류 수

total = 0

for _ in range(N):
    a, b = map(int, input().split())  # 가격, 개수
    total += a * b

if total == X:
    print("Yes")
else:
    print("No")