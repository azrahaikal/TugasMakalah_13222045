# ini adalah program untuk meng-konversi antara biner dan string/file

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def bits_to_text(bits, encoding='utf-8', errors='surrogatepass'):
    try:
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    except:
        return "[Error: Gagal konversi biner ke teks]"

def file_to_bits(file_path):
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
        # Konversi setiap byte ke 8-bit string
        return "".join(f"{byte:08b}" for byte in content)
    except Exception as e:
        print(f"Error membaca file: {e}")
        return None

def bits_to_file(bits, output_path):
    try:
        # Konversi string bit kembali ke byte array
        byte_array = bytearray()
        for i in range(0, len(bits), 8):
            byte_chunk = bits[i:i+8]
            if len(byte_chunk) == 8:
                byte_array.append(int(byte_chunk, 2))
        
        with open(output_path, 'wb') as f:
            f.write(byte_array)
        return True
    except Exception as e:
        print(f"Error menulis file: {e}")
        return False