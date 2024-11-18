gemeinsam = {}
d1 = {}
for x in range(32, 64):
    d1[x] = chr(x) 

for k1, v1 in d1.items():
   print(k1, v1)

d2={} 
for x in range(64, 96):
    d2[x] = chr(x) 
for k2, v2 in d1.items():
    
    d3 = {}
for x in range(96, 128):
    d3[x] = chr(x) 

for k3, v3 in d3.items():
    d3[x] = chr(x) 

    d4 = {}
for x in range(128, 160):
    d4[x] = chr(x) 

for k4, v4 in d4.items():
    d4[x] = chr(x) 

    d5 = {}
for x in range(160, 192):
    d5[x] = chr(x) 

for k5, v5 in d5.items():
   d5[x] = chr(x) 

d6 = {}
for x in range(192, 224):
    d6[x] = chr(x) 

for k6, v6 in d6.items():
   d6[x] = chr(x) 

d7 = {}
for x in range(224, 256):
    d7[x] = chr(x) 

for k7, v7 in d7.items():
    d7[x] = chr(x) 



    print(f"| {k1} | {v1} | {k2} | {v2} | {k3} | {v3} | {k4} | {v4} | {k5} | {v5} | {k6} | {v6} | {k7} | {v7} |")



'''
print("\nTabellarische Ausgabe:")
for (k1, v1), (k2, v2), (k3, v3), (k4, v4), (k5, v5), (k6, v6), (k7, v7) in zip(d1.items(), d2.items(), d3.items(), d4.items(), d5.items(), d6.items(), d7.items()):
    print(f"| {k1:2} | {v1:2} | {k2:2} | {v2:2} | {k3:2} | {v3:2} | {k4:2} | {v4:2} | {k5:2} | {v5:2} | {k6:2} | {v6:2} | {k7:2} | {v7:2} |")

multidimensional_dict = {
    'd1': d1,
    'd2': d2,
    'd3': d3,
    'd4': d4,
    'd5': d5,
    'd6': d6,
    'd7': d7
}
# Füge mehrere Dictionaries zusammen
gemeinsam = d1 | d2 | d3 | d4 | d5 | d6 | d7

#oder
gemeinsam.update(d1)
gemeinsam.update(d2)
gemeinsam.update(d3)
gemeinsam.update(d4)
gemeinsam.update(d5)
gemeinsam.update(d6)
gemeinsam.update(d7)

print(gemeinsam)
for key,value in gemeinsam.items():
    print(key, value)'''