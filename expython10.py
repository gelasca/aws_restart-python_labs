import re

with open("preproinsulin-seq.txt") as arquivo:
    texto = arquivo.read()
    resultados = re.findall('[a-z]+',texto)

resultados = ''.join(resultados)

with open('preproinsulin-seq-clean.txt','w') as arquivo:
    arquivo.write(resultados)

nome_cadeias = ['lsinsulin-seq-clean.txt','binsulin-seq-clean.txt','cinsulin-seq-clean.txt','ainsulin-seq-clean.txt']
indices_cadeias = [(0,24),(24,54),(54,89),(89,110)]

for x in range(4):
    with open(nome_cadeias[x],'w') as arquivo:
        arquivo.write(resultados[indices_cadeias[x][0]:indices_cadeias[x][1]])