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



# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)


# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
