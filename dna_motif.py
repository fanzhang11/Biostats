dna = "TCCTACGAGGTACATACGAGGGGTTACGAGGTACGAGGTACGAGGTGCGATACGAGGTGTATAGATCTACGAGGTTACGAGGTACGAGGTGACATTGTACGAGGGTACGAGGGTACGAGGGATACGAGGTTCAACCTAAATACGAGGGTTTTTACGAGGATACGAGGTACGAGGTACGAGGCTACGAGGTTTTACGAGGTACGAGGTACGAGGTTACGAGGGCACGTGTACGAGGCAAACACTACGAGGTACGAGGCCCTACGAGGATACGAGGCTACGAGGGGGGTACGAGGTACGAGGCGGAGGTACGAGGGGGTACGAGGTTGGTACGAGGGCGTACGAGGTACGAGGTACGAGGTACTACGAGGTACGAGGCTACGAGGTTACGAGGACTACGAGGATACGAGGTTGTTACGAGGTACGAGGCCGGGTCTGTCGATACGAGGATTACGAGGATTATACGAGGGACCCGATACGAGGAGACTACGAGGAATACGAGGGTATACGAGGTACGAGGTATTACGAGGTACGAGGTTACGAGGTTGGCTACGAGGCTACGAGGTACGAGGTACGAGGGCGTTACGAGGTACGAGGCTACGAGGCTACGAGGCGATACGAGGTACGAGGGGGAACGTACGAGGTTACGAGGTTACGAGGAGGTAGACGTACGAGGCCCGCTACGAGGTTACGAGGTACGAGGTGTTACGAGGTACGAGGGACTACGAGGTACGAGGTTACGAGGTACGAGGTACGAGGTACGAGGTACGAGGAGCATTACGAGGATACGAGGTACGAGGACTACGAGGCTACGAGGTGGGCTGTACGAGGCCCTTACGAGGGAGCATACGAGGTACGAGGTATACGAGG"
sub = "TACGAGGTA"


for i in range(len(dna)):
    match = dna[i:i+len(sub)]
    if match == sub:
        print(i+1)