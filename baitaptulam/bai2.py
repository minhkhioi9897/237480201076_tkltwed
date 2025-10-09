t = int(input("Nhập số giây: "))

gio = t // 3600 #1 gio bang 3600 giay
phut = (t % 3600) // 60#1 phut bang 60 giay
giay = t % 60

print(f"{gio}:{phut}:{giay}")
