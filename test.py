# spasi --> 0
# \t (tab) --> 1
def encode_whitespace(source_code, binary_message):
    lines = source_code.splitlines()
    encoded_lines = []
    
    # tiap baris 1 bit
    bit_index = 0
    message_len = len(binary_message)
    
    for line in lines:
        if bit_index < message_len:
            # ambil satu bit
            bit = binary_message[bit_index]
            suffix = " " if bit == "0" else "\t"
            encoded_lines.append(line + suffix)
            bit_index += 1
        else:
            # kalau pesan sudah habis, masukkan sisa source code aslinya
            encoded_lines.append(line)
            
    return "\n".join(encoded_lines)

# ekstrak spasi dan tab
def decode_whitespace(stego_code):
    lines = stego_code.splitlines()
    binary_result = ""
    
    for line in lines:
        if line.endswith(" "):
            binary_result += "0"
        elif line.endswith("\t"):
            binary_result += "1"
            
    return binary_result


# test kode
original_code = """print("Hello World")
x = 10
y = 20
print(x + y)
# end"""

# pesan yg ingin disisipkan
secret_bin = "1011"

# encode
stego_code = encode_whitespace(original_code, secret_bin)
print("Pesan sudah disispkan ke source code")
print(stego_code)

# decode
extracted_bin = decode_whitespace(stego_code)
print("\npesan berhasil diekstrak")
print(extracted_bin)