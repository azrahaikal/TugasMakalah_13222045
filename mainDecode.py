# mainDecode.py
import re
import os

def detect_comment_style_multi(line):
    # Hapus whitespace stego (spasi/tab) di ujung baris SEBELUM deteksi gaya
    text_stego_removed = line.rstrip(" \t")
    text_clean = text_stego_removed.replace('#', '').strip()
    
    if not text_clean:
        return ""
    
    # Ambil kata-kata (tapi jangan hilangkan _ dan - karena itu penanda biner)
    # Kita bandingkan dengan teks yang sudah di-lowercase untuk deteksi case-insensitive
    binary_extracted = ""
    words = text_clean.split()
    
    i = 0
    while i < len(words):
        w1 = words[i]
        
        # 1. Cek Snake Case (000) - misal: hello_world
        if '_' in w1:
            binary_extracted += "000"
            i += 1 # Snake case menggabungkan 2 kata jadi 1 token di split()
        # 2. Cek Kebab Case (001) - misal: hello-world
        elif '-' in w1:
            binary_extracted += "001"
            i += 1
        elif i + 1 < len(words):
            w2 = words[i+1]
            # 3. Cek blok 2-kata berdasarkan kapitalisasi
            if w1[0].islower() and w2[0].isupper():
                binary_extracted += "010" # camel Case
            elif w1[0].isupper() and w2[0].isupper():
                binary_extracted += "011" # Pascal Case
            elif w1[0].islower() and w2[0].islower():
                binary_extracted += "100" # 2 kata kecil
            elif w1[0].isupper() and w2[0].islower():
                binary_extracted += "101" # 2 kata, kata pertama kapital
            i += 2
        else:
            # 4. Cek blok 1-kata sisa
            if w1[0].isupper():
                binary_extracted += "110"
            else:
                binary_extracted += "111"
            i += 1
            
    return binary_extracted

def main_decode():
    stego_file = "output.txt"
    with open(stego_file, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        
    raw_binary = ""
    for line in lines:
        # EKSTRAK KOMENTAR DULU
        if line.strip().startswith("#"):
            raw_binary += detect_comment_style_multi(line)
            
        # EKSTRAK WHITESPACE KEMUDIAN
        suffix = ""
        idx = len(line) - 1
        while idx >= 0 and line[idx] in (" ", "\t"):
            suffix = line[idx] + suffix
            idx -= 1
        for char in suffix:
            raw_binary += "0" if char == " " else "1"

    # POTONG BERDASARKAN HEADER 32-BIT
    if len(raw_binary) >= 32:
        header_bits = raw_binary[:32]
        msg_len = int(header_bits, 2)
        final_msg = raw_binary[32 : 32 + msg_len]
        print(f"Pesan Biner: {final_msg}")
    else:
        print("Gagal mengekstrak header.")

if __name__ == "__main__":
    main_decode()