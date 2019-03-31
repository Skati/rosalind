def rna_(filepath):
    with open(filepath,'r') as file:
        for line in file:
            rna=line.replace('T','U')
            return rna
