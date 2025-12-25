# program ini untuk mengubah gaya penulisan komentar
# definisi 8 jenis komentar ada di deteksiKomentar.py:

def ubah_komentar(komentar_asli, biner_3_bit):
    # hilangkan simbol '#' dan spasi di
    clean_comment = komentar_asli.replace('#', '').strip()
    words = clean_comment.split()
    
    if len(words) == 0:
        return komentar_asli

    # menghandle 1 kata
    if len(words) == 1:
        w1 = words[0]
        # jika hanya 1 kata, kata kedua adalah kata pertama + ".."
        w2 = words[0] + ".."
    else:
        w1 = words[0]
        w2 = words[1]

    result = ""

    if biner_3_bit == "000":    # Snake_case
        result = f"{w1.lower()}_{w2.lower()}"
    elif biner_3_bit == "001":  # Kebab-case
        result = f"{w1.lower()}-{w2.lower()}"
    elif biner_3_bit == "010":  # camel Case
        result = f"{w1.lower()} {w2.capitalize()}"
    elif biner_3_bit == "011":  # Pascal Case
        result = f"{w1.capitalize()} {w2.capitalize()}"
    elif biner_3_bit == "100":  # 2 kata, semua non kapital
        result = f"{w1.lower()} {w2.lower()}"
    elif biner_3_bit == "101":  # 2 kata, kata pertama huruf pertama kapital
        result = f"{w1.capitalize()} {w2.lower()}"
    elif biner_3_bit == "110":  # 1 kata, kapital
        result = f"{words[0].capitalize()}"
    elif biner_3_bit == "111":  # 1 kata, non kapital
        result = f"{words[0].lower()}"
    
    return f"# {result}"

# ngetest
k1 = "# hello world"
print(f"Pascal Case (011): {ubah_komentar(k1, '011')}")
print(f"Camel Case (010) : {ubah_komentar(k1, '010')}")

k2 = "# hello"
print(f"Snake Case (000) : {ubah_komentar(k2, '000')}")
print(f"Pascal Case (011): {ubah_komentar(k2, '011')}") 
print(f"1 Kata kapital (110) : {ubah_komentar(k2, '110')}")