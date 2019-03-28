def dna(filepath):
    with open(filepath,'r') as file:
        for line in file:
            rna=line.replace('T','U')
            return rna
print(dna('/media/storage/dev/python/rosalind/data/rosalind_rna.txt'))
