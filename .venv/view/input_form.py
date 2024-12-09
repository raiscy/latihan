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

def input_data_mahasiswa():
    print("=== Form Input Data Mahasiswa ===")
    
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    jurusan = input("Masukkan Jurusan: ")
    
    while True:
        tahun_masuk = input("Masukkan Tahun Masuk (YYYY): ")
        if tahun_masuk.isdigit() and len(tahun_masuk) == 4:
            break
        else:
            print("Tahun masuk tidak valid. Harap masukkan tahun dalam format YYYY.")

    return Mahasiswa(nama, nim, jurusan, tahun_masuk)

def main():
    daftar_mahasiswa = []
    
    while True:
        mahasiswa = input_data_mahasiswa()
        daftar_mahasiswa.append(mahasiswa)

        lagi = input("Apakah Anda ingin menambahkan mahasiswa lain? (y/n): ")
        if lagi.lower() != 'y':
            break

    print("\n=== Informasi Semua Mahasiswa ===")
    for mhs in daftar_mahasiswa:
        mhs.tampilkan_info()
        print()  # Untuk memberi jarak antar mahasiswa

if __name__ == "__main__":
    main()