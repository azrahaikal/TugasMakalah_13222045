# ini adalah program utama untuk meng-encode pesan ke suatu source code
import os
import argparse
from ubahJenisKomentar import ubah_komentar_multi
from helperBiner import text_to_bits, file_to_bits

def encode_whitespace_chunk(line, binary_message, bit_index, bits_per_line, message_len):
    if bit_index < message_len:
        bit_chunk = binary_message[bit_index : bit_index + bits_per_line]
        suffix = "".join([" " if b == "0" else "\t" for b in bit_chunk])
        return line + suffix, bit_index + len(bit_chunk)
    return line, bit_index

def main_encode():
    print("ENCODER")
    
    print("Pilih jenis pesan yang ingin disembunyikan:")
    print("1. Pesan Teks String")
    print("2. File (.txt, .pdf, .docx, dll)")
    pilihan = input("Pilihan (1/2): ")
    
    secret_bin = ""
    
    if pilihan == "1":
        secret_text = input(">> Masukkan pesan rahasia: ")
        secret_bin = text_to_bits(secret_text)
    elif pilihan == "2":
        path_file = input(">> Masukkan path file (cth: dokumen.pdf): ")
        if not os.path.exists(path_file):
            print("[Error] File tidak ditemukan!")
            return
        print("Meng-konversi file ke biner...")
        secret_bin = file_to_bits(path_file)
        if not secret_bin: return
    else:
        print("[Error] Pilihan tidak valid.")
        return

    source_file = input(">> Masukkan nama file source code carrier (cth: sourceCode1.py): ")
    n_str = input(">> Jumlah bit spasi/tab per baris (Default 5): ")
    n_bits_whitespace = int(n_str) if n_str.strip() else 5
    
    if not os.path.exists(source_file):
        print(f"\n[Error] File '{source_file}' tidak ditemukan!")
        return

    base_name, ext = os.path.splitext(source_file)
    output_file = "output" + ext
    marker = "//" if ext in ['.c', '.cpp', '.h'] else "#"
    
    # header 32 bit yang merepresentasikan panjang pesan
    header = format(len(secret_bin), '032b')
    full_binary = header + secret_bin
    
    with open(source_file, "r") as f:
        lines = f.read().splitlines()
    
    encoded_lines = []
    bit_index = 0
    message_len = len(full_binary)
    
    print("\n")
    print(f"Total Ukuran Data: {len(secret_bin)} bits")

    # 1. mengisi di source code
    for line in lines:
        current_line = line.rstrip() 
        if current_line.strip().startswith(marker) and bit_index < message_len:
            current_line, bit_index = ubah_komentar_multi(current_line, full_binary, bit_index, marker=marker)
        
        current_line, bit_index = encode_whitespace_chunk(
            current_line, full_binary, bit_index, n_bits_whitespace, message_len
        )
        encoded_lines.append(current_line)
        
    if bit_index < message_len:
        print(f"menambahkan baris kosong untuk sisa pesan (source code terlalu pendek)...")
        
    # 2. mengisi di baris baru di paling bawah source code
    while bit_index < message_len:
        base_overflow_line = "" 
        
        encoded_overflow_line, bit_index = encode_whitespace_chunk(
            base_overflow_line, full_binary, bit_index, n_bits_whitespace, message_len
        )
        encoded_lines.append(encoded_overflow_line)
        
    # 3. tulis file
    with open(output_file, "w", encoding="utf-8", newline='') as f:
        content = "\n".join(encoded_lines) + "\n"
        f.write(content)
        
    print(f"\n[SUKSES] Hasil steganografi disimpan di: {output_file}")

if __name__ == "__main__":
    main_encode()