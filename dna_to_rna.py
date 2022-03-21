dna = input()
rna = ''

for letter in dna:
    if letter == "T":
        rna += "U"
    else:
        rna += letter

print(rna)
