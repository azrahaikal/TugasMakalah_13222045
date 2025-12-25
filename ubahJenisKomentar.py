# program ini untuk mengubah gaya penulisan komentar
# definisi 8 jenis komentar ada di deteksiKomentar.py:

def ubah_komentar(komentar_asli, biner_3_bit):
    # jika kurang dari 3 bit
    if len(biner_3_bit) < 3:
        return "#" 

    clean_comment = komentar_asli.replace('#', '').strip()
    words = clean_comment.split()
    
    if len(words) == 0:
        return "#"

    # menghandle 1 kata
    if len(words) == 1:
        w1 = words[0]
        w2 = words[0] + ".."
    else:
        w1 = words[0]
        w2 = words[1]

    result = ""
    # mapping 8 jenis komentar
    if biner_3_bit == "000":    # Snake_case
        result = f"{w1.lower()}_{w2.lower()}"
    elif biner_3_bit == "001":  # Kebab-case
        result = f"{w1.lower()}-{w2.lower()}"
    elif biner_3_bit == "010":  # camel Case
        result = f"{w1.lower()} {w2.capitalize()}"
    elif biner_3_bit == "011":  # Pascal Case
        result = f"{w1.capitalize()} {w2.capitalize()}"
    elif biner_3_bit == "100":  # 2 kata, non kapital
        result = f"{w1.lower()} {w2.lower()}"
    elif biner_3_bit == "101":  # 2 kata, kata pertama kapital
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