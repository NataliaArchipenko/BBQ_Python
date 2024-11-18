my_dic = {}
for n in range(32, 256):
    my_dic[n] = chr(n)

# Printing in rows of 8 and replacing non-printable characters with '-'
for i in range(32, 249, 8):
    for x in range(8):
        value = my_dic[i + x]
        value = value if value.isprintable() else "-"
        print(f"{i + x:3} | {value:<3}", end=" | ")
    print()