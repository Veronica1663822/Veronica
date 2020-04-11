from Utilities import file_reader, RNA_TO_PROTEIN_DICT

def from_rna_to_protein(string):
    codified = ""
    for i in range(0, len(string), 3):
        if string[i:i+3] in RNA_TO_PROTEIN_DICT.keys():
            value_to_add = RNA_TO_PROTEIN_DICT[string[i:i+3]]
            if value_to_add != "Stop":
                codified += value_to_add
            else:
                return codified


if __name__ == "__main__":

    s = file_reader("rosalind_prot.txt")[0]
    print(from_rna_to_protein(s))

