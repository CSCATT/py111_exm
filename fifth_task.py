"""
ATTA
ACTA
AGCA
ACAA

A
 C
  T
   A
"""
consensus = str()
original_list = ["ATTA", 'ACTA', 'AGCA', 'ACAA']

#original_list = ["OLAB", 'OCBB', 'aGCB', 'aCDA'] # only for test

k = 0
while k < 4:
    sp = str()
    for i in original_list:
        sp = sp + i[k]

    prom = {}
    for i in sp:
        if i not in prom:
            prom[i] = sp.count(i)

    letter = max(prom.values())
    for i in prom:
        if prom[i] == letter:
            consensus = consensus + i
    k += 1

print(consensus)