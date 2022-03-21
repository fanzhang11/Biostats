dna1 = "GTAAGCCCGACAATTAAAATCTTTCCTCCGGTAGGCAATCGAGTAAACCGACCCCAGTTAGCAAAATGGGAGGGTTTGTGTCGCCGACTACAGAAAGAGGTGAAGGAAATGCTCTCGCCTTCCCTGTTGCCCTATAGCGTTCGACAATCTCCCGCTTACGGTCATAATTGCGCCCTTCTGTCTGTGGGGAGCACACCTAGCCCTGCAATACGCTCATGAGGGGCTACAACCAAGCATTTGATCAGTCAACGGATCTCGGTTCTAGTGGGCGGTACCTACACTATGTCAAGAAATGCCTCACGCTAGGTCTCGCGGTCTCCGGCAGGCTACTCTGCCACTAGGGGCCAGATTGGTGGCTTTACACTGTTGTTTACATAGAAACGCCTAGGCGGGCGGCGGCCGGAGGTTCGGAGATGGGCAATTCGAGCATCCATTAAGCTAATATATAGGATCGCCGGCTAGAGATGAGTAGGCAGACACCCACATTTCTATTTCCAACAGACCTGAAAACTAAACTCCGTGCCGGTCACGCTGGGTTGCTCTCTTCCTCATTACCTGCACACCCTTATCAGCCGAAACTGCTTCATGAGAAACTCGAACACAGATGGGGGGACAGGGAATCTACTCAAAGGAGTCCTAGCTAGGGATACAGCGCATGTGGGTCAAGTCCCCAATGAATTAGAAAGAAGATGGCTAAGGTATACTTAGCATGCCAGTTTTGCCCACGCTGACCGTAGCAATCCTAGACTCGTGGTAGCTCGATAGGATTTAAAGCCGCCGCGCTCGTCGCATAAGTATGCTTTAATCATAGTCGGAACCACTCATGTCATTCGCCCAAGCAAAACTCACCGGCAAAGTTCTAAAATGCTCCTAAACGCTGGGCCGAGTCAAGGGAAGTAAGGGCTAGCCCACTGGCCTTAATCGGTACCAACGGCCGTGATGGCAAAGCCTCCATCGGACCTATACCATCGCCGAGTTGGGACA"
dna2 = "GTGAGCAGATTAATGAAATTCTTGGCCCTGCTAGGCTAATGGGTGCGTACGGTGGATTTAACAAAAGGGGTTGTTGTGTGGCGTCTGCCAACGTAAGCTGGAAAGGATATACTTTGTGGTTTCCAGTCAATTAAGGGCGCTCGAATAAACGCCCCAATGGGATACACCCTAGTGGTTGACGCACTGAGTGCGGAACTCAGAGCGTCGACAGGCTACCATGATGATCTATCAAATCTGTTGGCTCGCCAGCTGCTAAGGGCACCGATTTCTTTTGACTGAACGATGCAACCATCGGCCTCACGCTAGGATGCCGGACCGCCCCCCGCAAACTCGGCCCCTTCGCGACACAACCGAGATACGTCACTACTGGTTTCATAGCTCCGGCTTGGCGTTTAATATCTGGGGCTTCTCAGATAACCAAATAGACCCCCGTTGAAGCAACTACGTGGGCGTAACCGGTTGCGTCGATTAGCCAATCACCCGTAGTGCAAATTCGTCATCGTTGGAAACCGCAGCATCGTGCTGCAAAAGCCAAAACGAGCCCTTGCTACCAGCCTGTACAACGCTGTAGCGCGATGCTTACTTATGGTCGTCCCAGAATCATATGCGGGTTGATGCGGCGTAATCGAACCATTTACCGCGTTACGTGCCGCGCACGTGGGACAGTAGCGCCGCGGACGGTGACGAGGATGTCAAAGGTGGGTCTCGCTTGGAGGTTTCGTCCGAGGCCGATGGAACAACCCTTAACTTGCTTAATCTGGGTACGAATTACAGCGGGTTCGCATGTCGTATGTCCTATCATAAATTATCTGAGCATCCTGCTAAGCCAATACCCAGGCCAAAACCCGCAAGCGAGGTGCTCAAATGCGCCGATACGGATAACCCACACCAAGGATGGAACTTCTGCACCACTCGACATGAGGGAAACATACTTCCGGTAAGGCAAATACGTCGTGAAACCTATGCAGTAACTTTCTTGGACCA"

index = 0
hamming = 0

for letter in dna1:
    if letter != dna2[index]:
        hamming += 1
    index += 1

print(hamming)
        
    
