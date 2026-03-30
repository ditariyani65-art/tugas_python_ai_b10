# ================================
# FUNCTIONS
# ================================

def greet(nama: str) -> str:
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    return a + b


def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    return round(sum(angka) / len(angka), 2)


# ================================
# CLASS
# ================================

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai: list[float] = []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 75.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self):
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"


# ================================
# DEMO
# ================================

if __name__ == "__main__":

    print("=== FUNCTIONS ===")

    print(greet("haechan"))

    print("tambah(5, 7):", tambah(5, 7))
    print("tambah(10):", tambah(10))

    print("rata_rata([80, 90, 100]):", rata_rata([80, 90, 100]))
    print("rata_rata([]):", rata_rata([]))

    print("\n=== CLASS STUDENT ===")

    # Mahasiswa 1
    mhs1 = Student("jisung", "A123")
    mhs1.tambah_nilai(80)
    mhs1.tambah_nilai(85)
    mhs1.tambah_nilai(90)

    # Mahasiswa 2
    mhs2 = Student("jeno", "B456")
    mhs2.tambah_nilai(60)
    mhs2.tambah_nilai(75)
    mhs2.tambah_nilai(65)

    # Mahasiswa 3
    mhs3 = Student("mark", "B456")
    mhs3.tambah_nilai(90)
    mhs3.tambah_nilai(80)
    mhs3.tambah_nilai(85)

    # Cetak objek (pakai __str__)
    print(mhs1)
    print(mhs2)
    print(mhs3)

    # Cetak rata-rata & status
    print(f"{mhs1.nama} -> Rata-rata: {mhs1.rata_nilai()}, Status: {mhs1.status()}")
    print(f"{mhs2.nama} -> Rata-rata: {mhs2.rata_nilai()}, Status: {mhs2.status()}")
    print(f"{mhs3.nama} -> Rata-rata: {mhs3.rata_nilai()}, Status: {mhs3.status()}")