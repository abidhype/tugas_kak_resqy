
nilai_a = float(input("Masukkan Nilai A: "))
nilai_b = float(input("Masukkan Nilai B: "))

rata_rata = (nilai_a + nilai_b) / 2

if rata_rata >= 75:
    status = "Lulus"
else:
    status = "Tidak Lulus"

print(f"Nilai A: {nilai_a}")
print(f"Nilai B: {nilai_b}")
print(f"Rata-rata: {rata_rata}")
print(f"Status: {status}")