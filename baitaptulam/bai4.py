import math

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Tính chu vi và nửa chu vi
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f"Chu vi tam giác: {a + b + c}")
print(f"Diện tích tam giác: {s:.2f}")
