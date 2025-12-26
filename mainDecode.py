# ini adalah program utama untuk meng-decode
import os
import argparse
from helperBiner import bits_to_text, bits_to_file

def detect_comment_style_multi(line, marker="#"):
    line_clean = line.rstrip("\r\n")
    text_stego_removed = line_clean.rstrip(" \t")
    
    stripped_line = text_stego_removed.strip()
    if not stripped_line.startswith(marker): return ""
    
    text = stripped_line[len(marker):].strip()
    if not text: return ""
    
    tokens = text.split()
    binary_extracted = ""
    i = 0
    while i < len(tokens):
        w1 = tokens[i]
        if not any(c.isalpha() for c in w1):
            i += 1; continue
        if '_' in w1: binary_extracted += "000"; i += 1 
        elif '-' in w1: binary_extracted += "001"; i += 1
        elif w1.endswith(".."):
            if w1[0].isupper(): binary_extracted += "110"
            else: binary_extracted += "111"
            i += 1
        else:
            if i + 1 < len(tokens):
                w2 = tokens[i+1]
                w2_clean = w2.replace("..", "")
                has_dot_dot = w2.endswith("..")
                if has_dot_dot:
                    if w1[0].isupper() and w2_clean[0].isupper(): binary_extracted += "110"
                    elif w1[0].islower() and w2_clean[0].islower(): binary_extracted += "111"
                    elif w1[0].islower() and w2_clean[0].isupper(): binary_extracted += "010"
                    elif w1[0].isupper() and w2_clean[0].islower(): binary_extracted += "101"
                    else: binary_extracted += "100"
                else:
                    if w1[0].islower() and w2_clean[0].isupper(): binary_extracted += "010"
                    elif w1[0].isupper() and w2_clean[0].isupper(): binary_extracted += "011"
                    elif w1[0].islower() and w2_clean[0].islower(): binary_extracted += "100"
                    elif w1[0].isupper() and w2_clean[0].islower(): binary_extracted += "101"
                i += 2
            else: i += 1
    return binary_extracted

def main_decode():
    print("DECODER\n")

    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?", help="File stego")
    args = parser.parse_args()

    if args.file: stego_file = args.file
    else: stego_file = input("Masukkan nama file stego (output.py / output.c): ")
    
    if not os.path.exists(stego_file):
        print("[Error] File tidak ditemukan!"); return
        
    ext = os.path.splitext(stego_file)[1]
    marker = "//" if ext in ['.c', '.cpp', '.h'] else "#"
    
    print(f"Membaca {stego_file}...")
        
    with open(stego_file, "r", encoding="utf-8", newline='') as f:
        content = f.read()
        
    lines = content.split('\n')
        
    raw_binary = ""
    for line in lines:
        current_line = line.rstrip('\r')
        
        if current_line.strip().startswith(marker):
            raw_binary += detect_comment_style_multi(current_line, marker)
            
        suffix = ""
        idx = len(current_line) - 1
        while idx >= 0 and current_line[idx] in (" ", "\t"):
            suffix = current_line[idx] + suffix
            idx -= 1
        raw_binary += "".join(["0" if c == " " else "1" for c in suffix])

    if len(raw_binary) >= 32:
        header = raw_binary[:32]
        try:
            length = int(header, 2)
            msg_binary = ""
            
            # auto repair?
            if len(raw_binary) < 32 + length:
                 missing = (32 + length) - len(raw_binary)
                 print(f"[Warning] Data terpotong {missing} bits.")
                 # ditambal dengan '0'
                 print(f"[Auto-Repair] Menambahkan {missing} bit '0'...")
                 msg_binary = raw_binary[32:] + ("0" * missing)
            else:
                 msg_binary = raw_binary[32 : 32 + length]
            
            print(f"\nData Valid: {len(msg_binary)} bits.")
            print("Apa yang ingin dilakukan?")
            print("1. Tampilkan sebagai Teks")
            print("2. Simpan sebagai File (.txt, .pdf, .word, dll)")
            aksi = input("Pilihan (1/2): ")
            
            if aksi == "1":
                decoded_text = bits_to_text(msg_binary)
                print(f"\n[PESAN RAHASIA]:\n{decoded_text}")
            elif aksi == "2":
                out_filename = input("Masukkan nama file output (cth: rahasia.pdf): ")
                if bits_to_file(msg_binary, out_filename):
                    print(f"\n[SUKSES] File berhasil direkonstruksi: {out_filename}")
            else:
                print("Pilihan tidak valid.")
                
        except ValueError:
            print("[Error] Header biner tidak valid.")
    else:
        print(f"[Error] Biner terlalu pendek.")

if __name__ == "__main__":
    main_decode()