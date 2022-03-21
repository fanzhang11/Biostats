from Bio import Entrez


Entrez.email = "fanzhang1@utexas.edu"
handle = Entrez.esearch(
    db="nucleotide",
    term = '"Stenamma"[Organism] AND ("2010/05/19"[Publication Date] : "2011/01/30"[Publication Date])')
record = Entrez.read(handle)
print(record["Count"])
