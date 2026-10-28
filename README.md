## pertemuan 11 - Dictionary/Map

Nama: Siti Solehah
NIM: 2225250058
Kelas: 3B

## Tujuan

Mempelajari penggunaan dictionary dalam Python untuk menyimpan data dalam bentuk pasangan key-value, mengakses data menggunakan key, menambah dan mengubah data, menghapus data, serta menggunakan dictionary untuk mengelola data mahasiswa.

## Struktur Folder

pertemuan-11-dictionary-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_dictionary.py
│   ├── 02_akses_get.py
│   ├── 03_manipulasi_dictionary.py
│   ├── 04_iterasi_dictionary.py
│   ├── 05_dictionary_bersarang.py
│   └── 06_fungsi_dictionary.py
└── praktik/
    └── data_mahasiswa.py

## Struktur Data

Program menggunakan dictionary dengan NIM sebagai key utama. Setiap mahasiswa memiliki data berupa nama, kelas, dan nilai sebagai value. Dengan menggunakan dictionary, data mahasiswa dapat dicari berdasarkan NIM tanpa harus mencari melalui indeks list.

## Cara Menjalankan

Jalankan file latihan satu per satu melalui terminal VS Code.

Untuk menjalankan program utama, gunakan perintah:

python3 praktik/data_mahasiswa.py

## Test Case

No.| Input/Aksi| Hasil yang Diharapkan
1| Mencari NIM A003| Data Citra ditampilkan
2| Mencari NIM A999| Data tidak ditemukan
3| Mengubah nilai A002 menjadi 82| Nilai A002 berubah menjadi 82
4| Menambahkan mahasiswa A006| Data mahasiswa A006 tersimpan
5| Menampilkan seluruh data menggunakan "items()"| Semua NIM dan data mahasiswa ditampilkan
6| Menghitung rata-rata nilai| Rata-rata nilai seluruh mahasiswa ditampilkan

## Hasil Pengujian

Program menggunakan dictionary untuk menyimpan data mahasiswa. Pencarian dilakukan berdasarkan NIM, data baru ditambahkan dengan assignment, nilai mahasiswa diperbarui melalui key, dan seluruh data ditampilkan menggunakan "items()". Program juga menghitung rata-rata nilai mahasiswa.

## Refleksi

Dari praktik ini, saya memahami bahwa dictionary memudahkan pencarian dan pengelolaan data berdasarkan key. Kesalahan yang dapat terjadi adalah "KeyError" ketika mengakses key yang tidak tersedia. Untuk menghindarinya, saya menggunakan "get()" agar pencarian data lebih aman. Saya juga belajar menggunakan fungsi supaya program lebih terstruktur dan mudah diuji.