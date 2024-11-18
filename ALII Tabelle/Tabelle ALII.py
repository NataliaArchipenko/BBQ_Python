
d1 = {}
for x in range(32, 64):
    d1[x] = chr(x) 
d2={} 
for x in range(64, 96):
    d2[x] = chr(x) 
d3 = {}
for x in range(96, 128):
    d3[x] = chr(x) 
d4 = {}
for x in range(128, 160):
    d4[x] = chr(x) 
d5 = {}
for x in range(160, 192):
    d5[x] = chr(x) 
d6 = {}
for x in range(192, 224):
    d6[x] = chr(x) 
d7 = {}
for x in range(224, 256):
    d7[x] = chr(x) 

for (k1, v1), (k2,v2) , (k3,v3), (k4, v4), (k5, v5), (k6, v6), (k7, v7) in zip(d1.items(), d2.items(), d3.items(), d4.items(), d5.items(), d6.items(), d7.items()):

    #print(f"| {k1:^3} | {v1:^3} | {k2:^3} | {v2:^3} | {k3:^3} | {v3:^3} | {k4:^3} | {v4:^3} | {k5:^3} | {v5:^3} | {k6:^3} | {v6:^3} | {k7:^3} | {v7:^3} |")   
 # Überprüfen, ob es drückbar ist
    if v1.isprintable():
        v1 = v1
    else:
        v1 = "*"

    if v2.isprintable():
        v2 = v2
    else:
        v2 = "*"

    if v3.isprintable():
        v3 = v3
    else:
        v3 = "*"

    if v4.isprintable():
        v4 = v4
    else:
        v4 = "*"

    if v5.isprintable():
        v5 = v5
    else:
        v5 = "*"

    if v6.isprintable():
        v6 = v6
    else:
        v6 = "*"

    if v7.isprintable():
        v7 = v7
    else:
        v7 = "*"

    print(f"| {k1:^3} | {v1:^3} | {k2:^3} | {v2:^3} | {k3:^3} | {v3:^3} | {k4:^3} | {v4:^3} | {k5:^3} | {v5:^3} | {k6:^3} | {v6:^3} | {k7:^3} | {v7:^3} |")




