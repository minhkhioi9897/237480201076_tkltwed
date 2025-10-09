n = int(input("Nhập số nguyên dương n: "))

S = 0
for i in range(1, n + 1):
    S += i

print(f"Tổng S = 1 + 2 + ... + {n} = {S}")
