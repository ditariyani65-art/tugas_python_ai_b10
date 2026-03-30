# ================================
# 1. Deklarasi Variabel & Tipe Data
# ================================
nama = "Dita"          # string
umur = 21              # integer
tinggi = 149           # float
is_student = True      # boolean
hobi = ["makan", "tidur", "nonton anime", "musik", "nonton mv kp-op"]  # list

print("=== Deklarasi Variabel ===")
print(nama, umur, tinggi, is_student, hobi)

# ================================
# 2. Manipulasi String
# ================================
print("\n=== Manipulasi String ===")
teks1 = "Halo"
teks2 = "Dita"

gabung = teks1 + " " + teks2
print("Gabungan:", gabung)

print("Panjang string:", len(gabung))
print("Huruf besar:", gabung.upper())
print("Huruf kecil:", gabung.lower())

# ================================
# 3. Operasi Matematika
# ================================
print("\n=== Operasi Matematika ===")
a = 15
b = 5

print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian bulat:", a // b)
print("Sisa bagi:", a % b)

# ================================
# 4. List & Akses Elemen
# ================================
print("\n=== List ===")
buah = ["pir", "jeruk", "mangga", "anggur"]

print("List awal:", buah)
print("Elemen pertama:", buah[0])
print("Elemen terakhir:", buah[-1])

buah.append("melon")
print("Setelah tambah:", buah)

buah.remove("jeruk")
print("Setelah hapus jeruk:", buah)

buah.pop()
print("Setelah pop:", buah)

# ================================
# 5. Input User
# ================================
print("\n=== Input User ===")
nama_user = input("Masukkan nama kamu: ")
umur_user = input("Masukkan umur kamu: ")

print(f"Halo, nama saya {nama_user} dan umur saya {umur_user} tahun.")