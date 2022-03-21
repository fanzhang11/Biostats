dna = ''

file = open("C:/Users/Fan/Downloads/rosalind_orf.txt", "r")
for rawline in file:
    line = rawline.rstrip('\r\n') # remove returns
    dna += line
file.close()

rna = ''
complement = ''
rna_rev = ''

codon_table = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}
stop = ["UAA", "UAG", "UGA"]

# get rna seq
for letter in dna:
    if letter == "T":
        rna += "U"
    else:
        rna += letter

# get reverse complement 
for letter in rna:
    if letter == "A":
        complement += "U"
    elif letter == "U":
        complement += "A"
    elif letter == "C":
        complement += "G"
    elif letter == "G":
        complement += "C"
rna_rev = complement[::-1]

# list all frames
frames = [rna, rna[1:], rna[2:], rna_rev, rna_rev[1:], rna_rev[2:]]
frames_aa = []
pep_seq = ""
for i in frames:
    # find orf
    for j in range(0,len(i), 3):
        codon = i[j:j+3]
        if codon in codon_table.keys():
            pep_seq += codon_table[codon]
    frames_aa.append(pep_seq)
    pep_seq = ""

pep_stop = []
for sequence in frames_aa:
    cut_seq = sequence[:sequence.rfind('*')]
    pep_stop.append(cut_seq.split('*'))


orf_list = []
for splits in pep_stop:
    for seq in splits:
        for i in  range(len(seq)):
            if (seq[i] == 'M'):
                if seq[i:] not in orf_list:
                    print(seq[i:])
                    orf_list.append(seq[i:])



