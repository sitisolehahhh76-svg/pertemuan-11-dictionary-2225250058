data = {"nama": "siti solehah", "nilai": 85}

# Akses dengan get()
print(data.get("nama"))
print(data.get("kelas"))
print(data.get("kelas", "Belum diisi"))

# Memeriksa keberadaan key menggunakan operator 'in'
if "nilai" in data:
    print("Nilai tersedia.")