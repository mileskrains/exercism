def proteins(strand):
    cp = ('AUG Methionine UUU,UUC Phenylalanine UUA,UUG Leucine '
          'UCU,UCC,UCA,UCG Serine UAU,UAC Tyrosine UGU,UGC Cysteine '
          'UGG Tryptophan UAA,UAG,UGA STOP').split()
    cp_dict = {}
    for c, protein in zip(cp[::2], cp[1::2]):
        for codon in c.split(','):
            cp_dict[codon] = protein
    stop = False
    proteins = []
    while strand and not stop:
        codon, strand = strand[:3], strand[3:]
        protein = cp_dict[codon]
        if protein == 'STOP':
            stop = True
        else:
            proteins.append(protein)
    return proteins

