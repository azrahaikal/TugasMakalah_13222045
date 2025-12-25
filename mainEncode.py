import os
# Mengimpor fungsi multi-blok yang sudah diperbaiki
from ubahJenisKomentar import ubah_komentar_multi

def encode_whitespace_chunk(line, binary_message, bit_index, bits_per_line, message_len):
    """
    Menyisipkan n-bit melalui spasi/tab di akhir baris.
    """
    if bit_index < message_len:
        bit_chunk = binary_message[bit_index : bit_index + bits_per_line]
        # 0 -> Spasi, 1 -> Tab
        suffix = "".join([" " if b == "0" else "\t" for b in bit_chunk])
        return line + suffix, bit_index + len(bit_chunk)
    return line, bit_index

def main_encode():
    # --- KONFIGURASI ---
    source_file = "sourceCode1.py" 
    output_file = "output.txt"
    # Pesan biner contoh (Sesuaikan dengan pesan Anda)
    secret_bin = "101100111010110111000101" 
    n_bits_whitespace = 5 # Jumlah bit spasi/tab per baris
    
    # --- PROSES HEADER ---
    # Membuat header 32-bit yang menyimpan panjang asli pesan rahasia
    # Ini sangat penting agar decoder tidak membaca bit 'sampah' di akhir
    header = format(len(secret_bin), '032b')
    full_binary = header + secret_bin
    
    if not os.path.exists(source_file):
        print(f"Error: File {source_file} tidak ditemukan.")
        return

    with open(source_file, "r") as f:
        lines = f.read().splitlines()
    
    encoded_lines = []
    bit_index = 0
    message_len = len(full_binary)
    
    print(f"Memulai Encoding...")
    print(f"Panjang Pesan Asli: {len(secret_bin)} bit")
    print(f"Total dengan Header: {message_len} bit")

    for line in lines:
        current_line = line
        
        # 1. ENCODE GAYA KOMENTAR (Multi-Blok)
        # Mencoba menyisipkan 3 bit untuk setiap pasangan kata dalam komentar
        if line.strip().startswith("#") and bit_index < message_len:
            # Fungsi ini akan otomatis mengonsumsi bit sesuai jumlah kata yang tersedia
            current_line, bit_index = ubah_komentar_multi(line, full_binary, bit_index)
        
        # 2. ENCODE WHITESPACE (n-bit)
        # Sisipkan bit ke akhir baris menggunakan spasi dan tab
        current_line, bit_index = encode_whitespace_chunk(
            current_line, full_binary, bit_index, n_bits_whitespace, message_len
        )
        
        encoded_lines.append(current_line)
        
    # 3. OVERFLOW (Baris tambahan)
    # Jika pesan masih ada tetapi baris kode asli sudah habis
    while bit_index < message_len:
        empty_line, bit_index = encode_whitespace_chunk(
            "", full_binary, bit_index, n_bits_whitespace, message_len
        )
        encoded_lines.append(empty_line)
        
    # --- SIMPAN HASIL ---
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(encoded_lines))
    
    print(f"Selesai! Hasil steganografi disimpan di {output_file}")

if __name__ == "__main__":
    main_encode()