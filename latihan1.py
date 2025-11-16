data = []

while True:
    nama = input("Nama  : ")
    nim = input("NIM   : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    data.append([nama, nim, tugas, uts, uas, nilai_akhir])

    lanjut = input("Tambah data(y/t)? ").lower()
    if lanjut == 't':
        break

print("===============================================================")
print(f"| {'No':<2} | {'Nama':<10} | {'NIM':<10} | {'Tugas':<5} | {'UTS':<4} | {'UAS':<4} | {'Akhir':<7} |")
print("===============================================================")

no = 1
for d in data:
    print(f"| {no:<2} | {d[0]:<10} | {d[1]:<10} | {d[2]:<5} | {d[3]:<3} | {d[4]:<3} | {d[5]:<7.2f} |")
    no += 1
print("===============================================================")
