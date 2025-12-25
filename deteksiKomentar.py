# Ini adalah program untuk mendeteksi jenis penulisan komentar
# 1. Snake case: hello_world (dipisahkan oleh '_')                               ---> 000
# 2. Kebab case: hello-world (dipisahkan oleh '-')                               ---> 001
# 3. Camel case: hello World                                                     ---> 010
# 4. Pascal case: Hello World                                                    ---> 011
# 5. 2 kata dan semua huruf non-kapital: hello world                             ---> 100
# 6. 2 kata, lalu hanya huruf pertama di kata pertama yang kapital: Hello world  ---> 101
# 7. 1 kata dan huruf pertamanya kapital: Hello                                  ---> 110
# 8. 1 kata dan huruf pertamanya non-kapital: hello                              ---> 111
# asumsikan komentar ditulis dengan spasi

text = "Hello World"
textSplitted = text.split()
for word in textSplitted:
    if('_' in text):
        print("000")
    elif('-' in text):
        print("001")
    elif(textSplitted[0][0].isupper()):
        if(len(textSplitted) == 1):
            print("110")
        else:
            if(textSplitted[1][0].isupper()):
                print("011")
            else:
                print("101")
    else:
        if(len(textSplitted) == 1):
            print("111")
        else:
            if(textSplitted[1][0].isupper()):
                print("010")
            else:
                print("100")