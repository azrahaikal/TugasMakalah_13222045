# Tanggal   : 5 Juli 2023

# Deskripsi  
# Program akan menerima input jumlah siswa. Suatu barisan harus mengurut berdasarkan tinggi
# (yang paling pendek di paling depan). Program akan menentukan siapa siswa yang berada
# paling jauh dari posisi yang seharusnya



# KAMUS
# nSiswa                    : integer
# tinggiDiMonitor           : array of integer 
# tinggiSebenarnya          : array of integer
# tinggiSebenarnyaSorted    : array of integer
# idxMin, temp, count       : integer
# listJarak                 : array of integer
# maxJarak, maxIdxJarak     : integer
# finalMax                  : array of integer



# Algoritma
nSiswa = int(input("Masukkan jumlah siswa: "))
# Memasukkan tinggi badan
tinggiDiMonitor = [0 for i in range(nSiswa)]
for i in range(nSiswa):
        tinggiDiMonitor[i] = int(input(f"Masukkan tinggi siswa ke-{i+1} yang terlihat di monitor: "))


# Ubah tinggi di monitor, masukkan ke list tinggiSebenarnya
tinggiSebenarnya = [0 for i in range(nSiswa)]
for i in range(nSiswa):
    if tinggiDiMonitor[i] == 199:
        tinggiSebenarnya[i] = 188
    elif tinggiDiMonitor[i] == 198:
        tinggiSebenarnya[i] = 186
    elif tinggiDiMonitor[i] == 196:
        tinggiSebenarnya[i] = 189
        
    elif tinggiDiMonitor[i] == 189:
        tinggiSebenarnya[i] = 168
    elif tinggiDiMonitor[i] == 188:
        tinggiSebenarnya[i] = 166
    elif tinggiDiMonitor[i] == 186:
        tinggiSebenarnya[i] = 169
        
    elif tinggiDiMonitor[i] == 169:
        tinggiSebenarnya[i] = 198
    elif tinggiDiMonitor[i] == 168:
        tinggiSebenarnya[i] = 196
    elif tinggiDiMonitor[i] == 166:
        tinggiSebenarnya[i] = 199

    elif (tinggiDiMonitor[i]-6)%10 == 0:                # 1x6 --> 1x9
        tinggiSebenarnya[i] = tinggiDiMonitor[i] + 3
    elif (tinggiDiMonitor[i]-8)%10 == 0:                # 1x8 --> 1x6
        tinggiSebenarnya[i] = tinggiDiMonitor[i] - 2
    elif (tinggiDiMonitor[i]-9)%10 == 0:                # 1x9 --> 1x8
        tinggiSebenarnya[i] = tinggiDiMonitor[i] - 1
        
    elif ((tinggiDiMonitor[i] - (tinggiDiMonitor[i]%10))/10 == 18):          # 18x --> 16x
        tinggiSebenarnya[i] = 160 + (tinggiDiMonitor[i]%10)
    elif ((tinggiDiMonitor[i] - (tinggiDiMonitor[i]%10))/10 == 16):          # 16x --> 19x
        tinggiSebenarnya[i] = 190 + (tinggiDiMonitor[i]%10)
    elif ((tinggiDiMonitor[i] - (tinggiDiMonitor[i]%10))/10 == 19):          # 19x --> 18x
        tinggiSebenarnya[i] = 180 + (tinggiDiMonitor[i]%10)
        
    else:
        tinggiSebenarnya[i] = tinggiDiMonitor[i]


# Bikin template untuk tinggiSebenarnyaSorted
tinggiSebenarnyaSorted = [0 for i in range(nSiswa)]
for i in range(nSiswa):
    if tinggiDiMonitor[i] == 199:
        tinggiSebenarnyaSorted[i] = 188
    elif tinggiDiMonitor[i] == 198:
        tinggiSebenarnyaSorted[i] = 186
    elif tinggiDiMonitor[i] == 196:
        tinggiSebenarnyaSorted[i] = 189
        
    elif tinggiDiMonitor[i] == 189:
        tinggiSebenarnyaSorted[i] = 168
    elif tinggiDiMonitor[i] == 188:
        tinggiSebenarnyaSorted[i] = 166
    elif tinggiDiMonitor[i] == 186:
        tinggiSebenarnyaSorted[i] = 169
        
    elif tinggiDiMonitor[i] == 169:
        tinggiSebenarnyaSorted[i] = 198
    elif tinggiDiMonitor[i] == 168:
        tinggiSebenarnyaSorted[i] = 196
    elif tinggiDiMonitor[i] == 166:
        tinggiSebenarnyaSorted[i] = 199

    elif (tinggiDiMonitor[i]-6)%10 == 0:                # 1x6 --> 1x9
        tinggiSebenarnyaSorted[i] = tinggiDiMonitor[i] + 3
    elif (tinggiDiMonitor[i]-8)%10 == 0:                # 1x8 --> 1x6
        tinggiSebenarnyaSorted[i] = tinggiDiMonitor[i] - 2
    elif (tinggiDiMonitor[i]-9)%10 == 0:                # 1x9 --> 1x8
        tinggiSebenarnyaSorted[i] = tinggiDiMonitor[i] - 1
        
    elif ((tinggiDiMonitor[i] - (tinggiDiMonitor[i]%10))/10 == 18):          # 18x --> 16x
        tinggiSebenarnyaSorted[i] = 160 + (tinggiDiMonitor[i]%10)
    elif ((tinggiDiMonitor[i] - (tinggiDiMonitor[i]%10))/10 == 16):          # 16x --> 19x
        tinggiSebenarnyaSorted[i] = 190 + (tinggiDiMonitor[i]%10)
    elif ((tinggiDiMonitor[i] - (tinggiDiMonitor[i]%10))/10 == 19):          # 19x --> 18x
        tinggiSebenarnyaSorted[i] = 180 + (tinggiDiMonitor[i]%10)
        
    else:
        tinggiSebenarnyaSorted[i] = tinggiDiMonitor[i]


# Urutkan list tinggi sebenarnya
for i in range(nSiswa):
    idxMin = i
    for j in range(i+1, nSiswa):
        if tinggiSebenarnyaSorted[j]<tinggiSebenarnyaSorted[idxMin]:
            idxMin = j
            
    temp = tinggiSebenarnyaSorted[i]
    tinggiSebenarnyaSorted[i] = tinggiSebenarnyaSorted[idxMin]
    tinggiSebenarnyaSorted[idxMin] = temp            


listJarak = [0 for i in range(nSiswa)]

# Menghitung siapa yang berpindah paling jauh
count = 0            
for a in range(nSiswa):
    for b in range(nSiswa):
        if tinggiSebenarnya[a] == tinggiSebenarnyaSorted[b]:
                if (a-b>0):
                        listJarak[count] = a-b
                elif (b-a>0):
                        listJarak[count] = b-a
                count = count+1

maxJarak = listJarak[0]
maxIdxJarak = 0
finalMax = [-1, -1]

for i in range(nSiswa):
        if maxJarak < listJarak[i]:
                maxJarak = listJarak[i]
                maxIdxJarak = i

for i in range(nSiswa):
        if maxJarak == listJarak[i]:
                if finalMax[0] == -1:
                        finalMax[0] = i
                else:
                        finalMax[1] = i
                    
if maxJarak == 0:
    print(f"Semua siswa sudah berada di posisi yang tepat.")
elif finalMax[1] != -1:
    print(f"Yang berpindah paling jauh adalah orang ke-{finalMax[0]+1} dan ke-{finalMax[1]+1} pada urutan array di monitor: yaitu berpindah sejauh {maxJarak}.")
else:
    print(f"Yang berpindah paling jauh adalah orang ke-{finalMax[0]+1} pada urutan array di monitor: yaitu berpindah sejauh {maxJarak}.")