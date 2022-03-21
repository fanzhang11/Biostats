# takes input text file in FASTA format
# outputs text file with calculated frequencies
# for all 20 amino acids

# reads text file into a dictionary
def readfile(seq_file):
    prot_list = {}
    protein = ''
    aaseq = ''

    file = open(seq_file)
    for rawline in file:
        line = rawline.rstrip('\r\n') # remove returns
        # identifies lines containing protein name and location
        if line[0] == '>':
            # records previous key, value pair
            prot_list[protein] = aaseq
            # identifies new protein key
            protein = line[1:]
        else:
            # set new value as entire sequence
            # line by line
            aaseq += line
    file.close()
    # records final key, value pair
    prot_list[protein] = aaseq
    return prot_list

# writes new text file containing
# amino acid frequencies
def writefile(aadict):
    file = open('C:/Users/Fan/OneDrive/OD_Documents/Classes/BCH_394P/Homework/yeast_freq.txt', 'w')
    # first line are headers
    file.write('PROTEIN\tA\tC\tD\tE\tF\tG\tH\tI\tK\tL\tM\tN\tP\tQ\tR\tS\tT\tV\tW\tY\n')
    # iterate through sequences
    for key in aadict:
        file.write(key)
        # make vector of frequencies for each sequence
        vector = freq(aadict[key])
        # convert list vector into string
        for i in vector:
            file.write('\t' + i)
        # new line for each protein
        file.write('\n')
    file.close()

# calculates amino acid frequencies
# for a given sequence
def freq(sequence):
    # initialize dictionary of zeros
    freq_dict = dict.fromkeys(('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'))
    # initialize list vector of frequencies
    freq_vec = []
    for key in freq_dict:
        # change zeros to counts
        freq_dict[key] = sequence.count(key)
    total = sum(freq_dict.values())
    # sort to ensure same order
    # probably not needed
    for key in sorted (freq_dict.keys()):
        # get proportion
        freq = round(freq_dict[key] / total, 3)
        # add values to frequency vector
        freq_vec.append(str(freq))
    return freq_vec

prot_dict = readfile("C:/Users/Fan/OneDrive/OD_Documents/Classes/BCH_394P/Homework/yeast_aaseqs.txt")
# remove initial 'empty' key,value pair in dictionary
prot_dict.pop('', None)
writefile(prot_dict)



