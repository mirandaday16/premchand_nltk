import codecs

with codecs.open("Premchand.txt", 'r', encoding='utf-8', errors='ignore') as fdata:
    with open("premchandconverted.txt", 'w') as towel:
        towel.writelines(fdata.readlines())