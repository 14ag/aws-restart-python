from pathlib import Path
import re


# clean data
INSULIN_FILE=Path(__file__).parents[0] / "preproinsulin-seq.txt"

clean_data=[]
with open(INSULIN_FILE, "r", encoding="utf-8") as file:
    insulin_data=file.readlines() #line by line array

    for i in range(0,len(insulin_data)):
        data=insulin_data[i].strip()
        
        #remove leading numbers and surrounding spaces
        if len(data) > 7:
            entry=re.sub(r"\d+", "", data)
            clean_data.append(entry.strip())

for i in clean_data:
    print(i)

# Store the remaining sequence elements of human insulin in variables:
preproInsulin="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

lsInsulin="malwmrllpllallalwgpdpaaa"
bInsulin="fvnqhlcgshlvealylvcgergffytpkt"
aInsulin="giveqcctsicslyqlenycn"
cInsulin="rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin


# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin:")

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)
