data = {"nama": "siti solehah", "nilai": 85}

# Menambah dan mengubah data
data["kelas"] = "A"
data["nilai"] = 90
print("Setelah ditambah & diubah:", data)

# Menghapus data menggunakan pop
kelas = data.pop("kelas")
print("Data yang di-pop (kelas):", kelas)
print("Dictionary setelah pop:", data)