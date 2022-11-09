jenis = ["1. Sapi Warrior: 690 hari", "2. Sapi Mage: 420 hari", "3. Sapi Assasin: 530 hari", "4. Sapi Nolep: 330 hari"]

sWarrior = 690
sMage = 420
sAssasin = 530
sNolep = 330
jmlhari = 0

print("TOTAL WAKTU YANG DIBUTUHKAN AGAR SAPI DEWASA")
print("Keterangan: ")

for i in jenis:
    print(i)

while True:
    sapi = int(input("\nMasukkan kode sapi (1/2/3/4): "))
    byksapi = int(input("\nBerapa banyak sapi yang akan diinput: "))
    if sapi == 1:
        jmlhari += sWarrior*byksapi
    elif sapi == 2:
        jmlhari += sMage*byksapi
    elif sapi == 3:
        jmlhari += sAssasin*byksapi
    elif sapi == 4:
        jmlhari += sNolep*byksapi
    
    tanya = input("\nApakah ada lagi sapi yang ingin dihitung? (Y/T) ")
    if tanya == "Y" or tanya == "y":
        continue
    elif tanya == "T" or tanya == "t":
        break

y = int(jmlhari/365)
m = int((jmlhari%365)/30)
d = int((jmlhari%365)%30)
print(f"\nJadi total waktu yang dibutuhkan ialah {y} tahun {m} bulan {d} hari.")
       




