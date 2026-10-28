def cari_mahasiswa(data, nim):
    return data.get(nim, "Data tidak ditemukan")

def ubah_nilai(data, nim, nilai_baru):
    if nim in data:
        data[nim]["nilai"] = nilai_baru
        return True
    return False

mahasiswa_data = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78}
}

hasil = cari_mahasiswa(mahasiswa_data, "A002")
print("Hasil pencarian A002:", hasil)