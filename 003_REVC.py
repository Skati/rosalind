transtable = str.maketrans('acgtnACGTN', 'tgcanTGCAN')
def revc(filepath):
    with open(filepath,'r') as file:
        for line in file:
            revers= line.translate(transtable)[::-1]

            return revers


print(revc('/media/storage/dev/python/rosalind/data/rosalind_revc.txt'))
