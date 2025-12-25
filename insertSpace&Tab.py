# spasi --> 0
# \t (tab) --> 1

def encode_whitespace(source_code, binary_message, bits_per_line):
    # bits_per_line untuk menentukan jumlah bit pesan yang disisipkan di 1 baris
    lines = source_code.splitlines()
    encoded_lines = []
    
    bit_index = 0
    message_len = len(binary_message)
    
    # iterasi baris kode yang ada
    for line in lines:
        if bit_index < message_len:
            bit_chunk = binary_message[bit_index : bit_index + bits_per_line]
            suffix = "".join([" " if b == "0" else "\t" for b in bit_chunk])
            encoded_lines.append(line + suffix)
            bit_index += bits_per_line
        else:
            encoded_lines.append(line)
            
    # jika pesan ada, tetapi baris source code sudah habis
    while bit_index < message_len:
        bit_chunk = binary_message[bit_index : bit_index + bits_per_line]
        # buat baris baru di paling bawah
        empty_line_binary = "".join([" " if b == "0" else "\t" for b in bit_chunk])
        encoded_lines.append(empty_line_binary)
        bit_index += bits_per_line

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
print("Line 2")"""

secret_bin = "1011001110" 
n = 5 

# encode
stego_code = encode_whitespace(original_code, secret_bin, bits_per_line=n)

# decode
extracted_bin = decode_whitespace(stego_code)

print(f"Biner asli        : {secret_bin}")
print(f"Biner hasilekstrak: {extracted_bin}")
print(f"Apakah binernya cocok?  {secret_bin == extracted_bin}")

# print output stego
print("\n--- Struktur File Stego ---")
for line in stego_code.splitlines():
    print(repr(line))