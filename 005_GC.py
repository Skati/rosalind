import re
def gc(filename):
    data = open(filename, "r")
    dataset = data.read()
    pattern = re.compile('>Rosalind_\d{4}')
    stringnames = pattern.findall(dataset)
    result = pattern.split(dataset)
    emptydict = dict(zip(stringnames, result[1:]))
    print(emptydict)
    

gc('/media/storage/dev/python/rosalind/data/rosalind_gc.txt')
