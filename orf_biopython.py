from Bio.Seq import Seq

dna = ''
file = open("C:/Users/Fan/Downloads/rosalind_orf.txt", "r")
for rawline in file:
    line = rawline.rstrip('\r\n') # remove returns
    dna += line
file.close()

seq = Seq(dna)
table = 1
min_pro_len = 100

for strand, nuc in [(+1, seq), (-1, seq.reverse_complement())]:
    for frame in range(3):
        for pro in nuc[frame:].translate(table).split("*"):
            if len(pro) >= min_pro_len:
                print("%s...%s - length %i, strand %i, frame %i" % (pro[:30], pro[-3:], len(pro), strand, frame))
