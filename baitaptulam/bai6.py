import math

r = float(input("Nhập bán kính hình trụ (r): "))
h = float(input("Nhập chiều cao hình trụ (h): "))

dien_tich = 2 * math.pi * r * (h + r)
the_tich = math.pi * r**2 * h

print(f"\nDiện tích toàn phần của hình trụ: {dien_tich:.2f}")
print(f"Thể tích của hình trụ: {the_tich:.2f}")
