dna = input()
complement = ''

for letter in dna:
    if letter == "A":
        complement += "T"
    elif letter == "T":
        complement += "A"
    elif letter == "C":
        complement += "G"
    elif letter == "G":
        complement += "C"

rev_complement = complement[::-1]
print(rev_complement)
