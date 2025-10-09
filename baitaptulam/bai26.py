# Nhập số nguyên dương n từ người dùng
try:
    n = int(input("Nhập vào số nguyên dương n: "))

    if n > 0 and (n & (n - 1)) == 0:
        print(f"{n} là một số có dạng 2^k.")
    else:
        print(f"{n} không phải là số có dạng 2^k.")

except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")