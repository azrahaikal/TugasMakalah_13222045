# ini adalah program untuk mengubah gaya penulisan komentar berdasarkan input biner tertentu

def transformasi_blok(w1, w2, biner_3_bit):
    """Mengubah gaya pasangan kata."""
    w2_clean = w2.replace("..", "")
    
    if biner_3_bit == "000":    return f"{w1.lower()}_{w2_clean.lower()}"
    elif biner_3_bit == "001":  return f"{w1.lower()}-{w2_clean.lower()}"
    elif biner_3_bit == "010":  return f"{w1.lower()} {w2_clean.capitalize()}"
    elif biner_3_bit == "011":  return f"{w1.capitalize()} {w2_clean.capitalize()}"
    elif biner_3_bit == "100":  return f"{w1.lower()} {w2_clean.lower()}"
    elif biner_3_bit == "101":  return f"{w1.capitalize()} {w2_clean.lower()}"
    elif biner_3_bit == "110":  return f"{w1.capitalize()} {w2_clean.capitalize()}.."
    elif biner_3_bit == "111":  return f"{w1.lower()} {w2_clean.lower()}.."
    return None

def ubah_komentar_multi(komentar_asli, binary_message, bit_index, marker="#"):
    indent = komentar_asli[:len(komentar_asli) - len(komentar_asli.lstrip())]
    content = komentar_asli.strip()
    
    if not content.startswith(marker):
        return komentar_asli, bit_index
        
    clean_content = content[len(marker):].strip()
    words = clean_content.split()
    
    if not words:
        return f"{indent}{marker}", bit_index

    result_words = []
    i = 0
    message_len = len(binary_message)

    while i < len(words):
        w1 = words[i]
        
        if not any(c.isalpha() for c in w1):
            result_words.append(w1)
            i += 1
            continue

        if bit_index + 3 <= message_len:
            consumed_w2 = False
            if i + 1 < len(words) and any(c.isalpha() for c in words[i+1]):
                w2 = words[i+1]
                consumed_w2 = True
            else:
                w2 = w1 + ".." 
                consumed_w2 = False
            
            chunk = binary_message[bit_index:bit_index+3]
            transformed = transformasi_blok(w1, w2, chunk)
            
            if transformed:
                result_words.append(transformed)
                bit_index += 3
                i += 2 if consumed_w2 else 1
            else:
                result_words.append(w1)
                i += 1
        else:
            result_words.append(w1)
            i += 1
            
    return f"{indent}{marker} " + " ".join(result_words), bit_index