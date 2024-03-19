sonhap = int(input("Nhập số cần tính giai thừa : "))
giaithua = 1

i = 1
while i <= sonhap:
    giaithua *= i
    i += 1

print(f"Giai thừa của {sonhap} là : {giaithua}")

