class Mahasiswa:
    def __init__(self, nama, nim, jurusan, tahun_masuk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.tahun_masuk = tahun_masuk

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f"Tahun Masuk: {self.tahun_masuk}")

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek mahasiswa
    mahasiswa1 = Mahasiswa("Raifa Scylla Putri Widjaya", "312410204", "Teknik Informatika", 2024)
    mahasiswa2 = Mahasiswa("Kim Mingyu", "1234567", "Sistem Informasi", 2021)

    # Menampilkan informasi mahasiswa
    mahasiswa1.tampilkan_info()
    print()  # Untuk memberi jarak
    mahasiswa2.tampilkan_info()