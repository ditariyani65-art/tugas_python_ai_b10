# ================================
# IMPORT & SETUP
# ================================
import numpy as np
import pandas as pd
import os

np.random.seed(42)

# ================================
# NUMPY – DATA & STATISTIK
# ================================
nilai_ujian = np.random.randint(50, 100, size=15)

rata2 = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)

# ================================
# PANDAS – DATAFRAME
# ================================
data = {
    "nama": ["mark", "renjun", "haechan", "jeno", "jaemin", "chenle", "jisung"],
    "nim": ["001", "002", "003", "004", "005", "006", "007"],
    "nilai": nilai_ujian[:7]
}

df = pd.DataFrame(data)

# tambah kolom status
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 75 else "TIDAK LULUS")

# ================================
# FILE I/O
# ================================
def tulis_ringkasan(path):
    with open(path, "w") as f:
        f.write("=== RINGKASAN STATISTIK ===\n")
        f.write(f"Rata-rata: {rata2:.2f}\n")
        f.write(f"Median: {median}\n")
        f.write(f"Standar Deviasi: {std:.2f}\n")
        f.write(f"Nilai Min: {nilai_min}\n")
        f.write(f"Nilai Max: {nilai_max}\n\n")

        f.write("=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah data: {len(df)}\n")
        f.write(f"Jumlah LULUS: {(df['status'] == 'LULUS').sum()}\n")
        f.write(f"Jumlah TIDAK LULUS: {(df['status'] == 'TIDAK LULUS').sum()}\n")


# ================================
# OOP – GRADEBOOK
# ================================
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return float(self.df["nilai"].mean())

    def pass_rate(self, threshold: float = 75.0) -> float:
        lulus = (self.df["nilai"] >= threshold).sum()
        return (lulus / len(self.df)) * 100

    def save_summary(self, path: str):
        with open(path, "a") as f:
            f.write("\n=== GRADEBOOK ===\n")
            f.write(f"Average: {self.average():.2f}\n")
            f.write(f"Pass Rate: {self.pass_rate():.2f}%\n")

    def __str__(self):
        return f"GradeBook(jumlah_data={len(self.df)}, rata-rata={self.average():.2f})"


# ================================
# DEMO
# ================================
if __name__ == "__main__":

    print("=== NUMPY ===")
    print("Data:", nilai_ujian)
    print("Rata-rata:", rata2)
    print("Median:", median)
    print("Std Dev:", std)
    print("Min:", nilai_min)
    print("Max:", nilai_max)

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)

    print(gb)
    print("Average:", gb.average())
    print("Pass Rate:", gb.pass_rate(), "%")

    # simpan ke file
    file_path = "ringkasan_tugas6.txt"
    tulis_ringkasan(file_path)
    gb.save_summary(file_path)

    print("\nRingkasan disimpan ke:", file_path)