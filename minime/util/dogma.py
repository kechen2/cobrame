amino_acids = {
    "A": "ala__L_c",
    "R": "arg__L_c",
    "N": "asn__L_c",
    "D": "asp__L_c",
    "C": "cys__L_c",
    "E": "glu__L_c",
    "Q": "gln__L_c",
    "G": "gly_c",
    "H": "his__L_c",
    "I": "ile__L_c",
    "L": "leu__L_c",
    "K": "lys__L_c",
    "M": "met__L_c",
    "F": "phe__L_c",
    "P": "pro__L_c",
    "S": "ser__L_c",
    "T": "thr__L_c",
    "W": "trp__L_c",
    "Y": "tyr__L_c",
    "V": "val__L_c"
}

codon_table = {"TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L", "TCT": "S",
               "TCC": "S", "TCA": "S", "TCG": "S", "TAT": "Y", "TAC": "Y",
               "TAA": '*', "TAG": '*', "TGT": "C", "TGC": "C", "TGA": '*',
               "TGG": "W", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
               "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAT": "H",
               "CAC": "H", "CAA": "Q", "CAG": "Q", "CGT": "R", "CGC": "R",
               "CGA": "R", "CGG": "R", "ATT": "I", "ATC": "I", "ATA": "I",
               "ATG": "M", "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
               "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGT": "S",
               "AGC": "S", "AGA": "R", "AGG": "R", "GTT": "V", "GTC": "V",
               "GTA": "V", "GTG": "V", "GCT": "A", "GCC": "A", "GCA": "A",
               "GCG": "A", "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
               "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

transcription_table = {"A": "ump_c", "T": "amp_c", "C": "gmp_c", "G": "cmp_c"}

base_pairs = {"A": "T", "T": "A", "G": "C", "C": "G"}


def reverse_transcribe(seq):
    return ''.join(base_pairs[i] for i in reversed(seq))
