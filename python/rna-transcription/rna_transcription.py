def to_rna(dna_strand):
    transcriptions = {'G': 'C',
                      'C': 'G',
                      'T': 'A',
                      'A': 'U'}
    if set(dna_strand) - set('ACGT'):
        raise ValueError('Invalid nucleotide given')
    rna_strand = [transcriptions[nt] for nt in dna_strand]
    rna_strand = ''.join(rna_strand)
    return rna_strand

