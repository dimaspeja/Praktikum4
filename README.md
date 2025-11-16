# Menambahkan Data MAHASISWA
Membuat list kosong untuk menyimpan semua data mahasiswa. data[]

Nantinya setiap mahasiswa disimpan dalam bentuk list kecil di dalam data.

membuat perulangan tanpa batas dengan while true

Perulangan berhenti hanya jika diberi perintah break.


Meminta masukan pengguna:

nama → string

nim → string

tugas, uts, uas → diubah ke float (agar bisa pakai desimal)

Menghitung nilai akhir berdasarkan bobot:

Tugas = 30%

UTS = 35%

UAS = 35%

Hasil disimpan di nilai_akhir.

Data mahasiswa dimasukkan ke list data dalam bentuk list kecil dengan kdoe data.append

Program bertanya apakah ingin menambah data lagi dengan y/t

.lower() memastikan karakter selalu huruf kecil.

Jika jawaban t, perulangan berhenti.

Mencetak garis dan header tabel agar tampil rapi

lalu menggunakan loop for untuk Menampilkan Isi Tabel

no = 1 → nomor awal

for d in data: → mengambil satu data mahasiswa dari list utama

{no:<2} → rata kiri, lebar 2 karakter

{d[0]:<10} → nama (rata kiri, 10 karakter)

{d[1]:<6} → NIM

{d[2]:<5} → nilai tugas

{d[5]:<7.2f} → nilai akhir dengan 2 angka desimal
