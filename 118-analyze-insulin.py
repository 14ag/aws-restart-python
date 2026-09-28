import re
from pathlib import Path

txt="preproinsulin-seq.txt"

FILE_PATH=Path(__file__).parents[0] / txt
preproinsulin_clean=[]

# print(FILE_PATH)

with open(FILE_PATH, 'r') as file:
    preproinsulin=file.readlines()
    for i in preproinsulin:
        if len(i.strip()) > 7:
            entry=re.sub(r"\d+", "", i)
            preproinsulin_clean.append(entry.strip().replace(" ",""))
            print(preproinsulin_clean)

for i in preproinsulin_clean:
    print(len(i))

with open('preproinsulin-seq-clean.txt', 'w') as file:
    file.writelines(f"{line}\n" for line in preproinsulin_clean)

big_amino_acid="".join(line for line in preproinsulin_clean)

print(big_amino_acid[1])


def breakdown(a_acid,start,stop,filename):
    start-=1
    acid="".join(a_acid[i] for i in range(start,stop))
    
    with open(filename,'w') as file:
        file.write(acid)

breakdown(big_amino_acid,1,24,"lsinsulin-seq-clean.txt")
breakdown(big_amino_acid,25,54,"binsulin-seq-clean.txt")
breakdown(big_amino_acid,55,89,"cinsulin-seq-clean.txt")
breakdown(big_amino_acid,90,110,"ainsulin-seq-clean.txt")

