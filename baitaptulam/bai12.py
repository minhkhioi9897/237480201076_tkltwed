print("Giải và biện luận phương trình bậc nhất y = ax + b")

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm (đúng với mọi x).")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print(f"Phương trình có nghiệm duy nhất: x = {x:.2f}")
