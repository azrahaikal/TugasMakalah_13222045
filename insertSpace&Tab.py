# spasi --> 0
# \t (tab) --> 1

from ubahJenisKomentar import ubah_komentar

def encode_full_stego(source_code, binary_message, bits_per_line):
    lines = source_code.splitlines()
    encoded_lines = []
    bit_index = 0
    message_len = len(binary_message)

    for line in lines:
        current_line = line
        
        # cek apakah baris termasuk komentar
        if line.strip().startswith("#") and bit_index < message_len:
            # ambil 3 bit untuk gaya komentar
            comment_bits = binary_message[bit_index : bit_index + 3]
            # update isi baris gaya oenulisan komentar baru
            current_line = ubah_komentar(line, comment_bits)
            bit_index += len(comment_bits)
        
        # sisipkan space/tab
        if bit_index < message_len:
            bit_chunk = binary_message[bit_index : bit_index + bits_per_line]
            suffix = "".join([" " if b == "0" else "\t" for b in bit_chunk])
            encoded_lines.append(current_line + suffix)
            bit_index += len(bit_chunk)
        else:
            encoded_lines.append(current_line)

    # tulis di baris paling bawah
    while bit_index < message_len:
        bit_chunk = binary_message[bit_index : bit_index + bits_per_line]
        suffix = "".join([" " if b == "0" else "\t" for b in bit_chunk])
        encoded_lines.append(suffix)
        bit_index += len(bit_chunk)

    # tulis ke .txt
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(encoded_lines))
            
    return "\n".join(encoded_lines)

def decode_whitespace(stego_code):
    lines = stego_code.splitlines()
    binary_result = ""
    
    for line in lines:
        suffix = ""
        idx = len(line) - 1
        while idx >= 0 and line[idx] in (" ", "\t"):
            suffix = line[idx] + suffix
            idx -= 1
            
        # ubah ke biner
        for char in suffix:
            binary_result += "0" if char == " " else "1"
            
    return binary_result

# tes dengan 2 baris
original_code = """print("Line 1")
# ini komentar
print("Line 2")"""

secret_bin = "1011001110" 
n = 5 

# encode
stego_code = encode_full_stego(original_code, secret_bin, bits_per_line=n)

# decode
extracted_bin = decode_whitespace(stego_code)

print(f"Biner asli        : {secret_bin}")
print(f"Biner hasilekstrak: {extracted_bin}")
print(f"Apakah binernya cocok?  {secret_bin == extracted_bin}")

# print output stego
print("\n--- Struktur File Stego ---")
for line in stego_code.splitlines():
    print(repr(line))