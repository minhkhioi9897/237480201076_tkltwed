# Nhập dữ liệu
quang_duong = float(input("Nhập quãng đường (km): "))
van_toc = float(input("Nhập vận tốc xe (km/h): "))

# Kiểm tra vận tốc hợp lệ
if van_toc <= 0:
    print("Vận tốc phải lớn hơn 0!")
else:
    # Tính thời gian = quãng đường / vận tốc
    thoi_gian = quang_duong / van_toc

    # Đổi sang giờ và phút
    gio = int(thoi_gian)
    phut = (thoi_gian - gio) * 60

    print(f"\nThời gian xe đi hết quãng đường là: {thoi_gian:.2f} giờ")
    print(f"Hoặc: {gio} giờ {phut:.0f} phút")
