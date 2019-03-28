
actg=['A','C','T','G']
def dna(filepath):
    with open(filepath,'r') as file:
        for line in file:
            a=line.count('A')
            c=line.count('C')
            g=line.count('G')
            t=line.count('T')
            result=[]
            result.append(a,c,g,t)
            return result
print(dna('/media/storage/dev/python/rosalind/data/rosalind_dna.txt'))
