# ubahJenisKomentar.py

def transformasi_blok(w1, w2, biner_3_bit):
    """Mengubah gaya satu pasangan kata berdasarkan 3 bit."""
    if biner_3_bit == "000":    # Snake_case
        return f"{w1.lower()}_{w2.lower()}"
    elif biner_3_bit == "001":  # Kebab-case
        return f"{w1.lower()}-{w2.lower()}"
    elif biner_3_bit == "010":  # camel Case
        return f"{w1.lower()} {w2.capitalize()}"
    elif biner_3_bit == "011":  # Pascal Case
        return f"{w1.capitalize()} {w2.capitalize()}"
    elif biner_3_bit == "100":  # 2 kata kecil
        return f"{w1.lower()} {w2.lower()}"
    elif biner_3_bit == "101":  # 2 kata, kata pertama kapital
        return f"{w1.capitalize()} {w2.lower()}"
    elif biner_3_bit == "110":  # 1 kata kapital (kasus sisa)
        return f"{w1.capitalize()}"
    elif biner_3_bit == "111":  # 1 kata kecil (kasus sisa)
        return f"{w1.lower()}"
    return f"{w1} {w2}"

def ubah_komentar_multi(komentar_asli, binary_message, bit_index):
    """Memproses seluruh kata dalam baris komentar secara berpasangan."""
    clean_comment = komentar_asli.replace('#', '').strip()
    words = clean_comment.split()
    
    if not words:
        return "#", bit_index

    result_words = []
    i = 0
    message_len = len(binary_message)

    while i < len(words):
        # Jika masih ada minimal 3 bit biner tersedia
        if bit_index + 3 <= message_len:
            chunk = binary_message[bit_index:bit_index+3]
            w1 = words[i]
            
            if i + 1 < len(words):
                w2 = words[i+1]
                result_words.append(transformasi_blok(w1, w2, chunk))
                i += 2
            else:
                # Kasus jika hanya sisa 1 kata di baris tersebut
                result_words.append(transformasi_blok(w1, w1 + "..", chunk))
                i += 1
            bit_index += 3
        else:
            # Jika biner habis, masukkan sisa kata asli
            result_words.append(words[i])
            i += 1
            
    return "# " + " ".join(result_words), bit_index