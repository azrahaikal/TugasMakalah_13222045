# ini adalah file untuk mengubah gaya penulisan komentar berdasarkan input binary

inputt = "000001"

komentar = "terdiri dari empat kata"

# snake case: hello_world
def snakeCase(komentar:str, idxKomentar:int):
    return komentar[idxKomentar] + "_" + komentar[idxKomentar+1] + " "