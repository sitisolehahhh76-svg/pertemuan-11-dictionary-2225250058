# Dictionary Bersarang
mahasiswa_bersarang = {
    "A001": {"nama": "ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78},
    "A003": {"nama": "Citra", "nilai": 92}
}

print(mahasiswa_bersarang["A002"]["nama"])
print(mahasiswa_bersarang["A003"]["nilai"])

# Dictionary dengan List sebagai Value
rekap_nilai = {
    "Ayu": [80, 85, 90],
    "Budi": [70, 75, 78]
}

print("Nilai Ayu:", rekap_nilai["Ayu"])
print("Rata-rata Ayu:", sum(rekap_nilai["Ayu"]) / len(rekap_nilai["Ayu"]))