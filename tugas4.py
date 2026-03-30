# ================================
# 1. LIST – Akses & Manipulasi
# ================================
print("=== LIST ===")

data = ["pir", 15, "jeruk", 2.5, "mangga", 8]
print("List awal:", data)

print("Elemen pertama:", data[0])
print("Elemen terakhir:", data[-1])
print("Slicing [1:5:2]:", data[1:5:2])

# manipulasi
print("\nSebelum manipulasi:", data)
data.append("pisang")
data.insert(1, "anggur")
data.extend([100, "melon"])
data.remove("pir")
data.pop()

print("Sesudah manipulasi:", data)

# ================================
# 2. TUPLE – Immutability & Unpacking
# ================================
print("\n=== TUPLE ===")

data_tuple = ("Dita", 21, "Medan", "Mahasiswa", "Informatika")
print("Tuple:", data_tuple)

print("Panjang tuple:", len(data_tuple))
print("Akses indeks ke-2:", data_tuple[2])

# unpacking
nama, umur, *lainnya = data_tuple
print("Nama:", nama)
print("Umur:", umur)
print("Lainnya:", lainnya)

# ================================
# 3. SET – Operasi Himpunan
# ================================
print("\n=== SET ===")

set1 = {1, 2, 3, 4, 5, 5}
set2 = {4, 5, 6, 7, 8}

print("Set1:", set1)
print("Set2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# ================================
# 4. DICTIONARY
# ================================
print("\n=== DICTIONARY ===")

mahasiswa = {
    "nama": "Dita",
    "nim": "71230915044",
    "angkatan": 2023,
    "kota": "Medan"
}

print("Data awal:", mahasiswa)

# tambah
mahasiswa["jurusan"] = "Informatika"

# ubah
mahasiswa["kota"] = "medan"

# hapus
del mahasiswa["angkatan"]

print("Setelah perubahan:", mahasiswa)

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("\nIterasi:")
for key, value in mahasiswa.items():
    print(key, ":", value)

# ================================
# 5. NESTED STRUCTURES
# ================================
print("\n=== NESTED STRUCTURES ===")

buku = [
    {"judul": "Python Dasar", "penulis": "A", "tahun": 2020},
    {"judul": "AI Modern", "penulis": "B", "tahun": 2023},
    {"judul": "Data Science", "penulis": "C", "tahun": 2022},
    {"judul": "Machine Learning", "penulis": "D", "tahun": 2024}
]

print("Daftar Judul Buku:")
for b in buku:
    print(b["judul"])

# filter
buku_baru = [b for b in buku if b["tahun"] >= 2022]
print("\nBuku tahun >= 2022:")
for b in buku_baru:
    print(b["judul"], "-", b["tahun"])

# ================================
# 6. COMPREHENSION
# ================================
print("\n=== COMPREHENSION ===")

angka = list(range(1, 21))

genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]

print("Angka genap:", genap)
print("Kuadrat:", kuadrat)

# dict comprehension
dict_angka = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("Dict angka:", dict_angka)

# set comprehension
kalimat = "Saya Belajar Python"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print("Huruf unik:", huruf_unik)

# ================================
# 7. KEANGGOTAAN & PENCARIAN
# ================================
print("\n=== KEANGGOTAAN ===")

cek_list = ["pir", "jeruk", "mangga"]

if "jeruk" in cek_list:
    print("jeruk ada di list, index:", cek_list.index("jeruk"))
else:
    print("jeruk tidak ada")

cek_set = {1, 2, 3, 4}

if 3 in cek_set:
    print("3 ada di set")
else:
    print("3 tidak ada")