def main():
    #Establish an input string variable and an empty string variable
    DNA = "TAGATTCATCCCCTAGCATCTATCATCAGTTTGCTTACAACTGAGGACATGTAACCCCACGCGTCCAACCGTTAATCCATTCGTAAGCCTGCCGCGCTAATACCTATACAATCGGTCTCGGTTTTGTCAGCTCTGGCCGCCTATCACAATGTATGTTTCGTCGCGTCCAAGGTCCTTAGCCTATATCGACGTTCTTCGTGTTAGACGCATCGCGGGGGGAAACTAGATTGCGCGTAGATAGTGGCGCGCTGCCCGTTAGATTGGACTCAATGTGAGAGTACAGGTTCGTTATCCAGGCAAATAATACGAGTGCTGCGAATCCAGAACGTACTCAGTCCTAGCCAAATACTCCAAATGATAAGTGATCTTTACATGATTCTATTATGCAGCGCGGGAAACGATCGAAGTAAATCCTACGTCTGGTGGTATAACACCTCGCCAGGGGCGGGTCACCCTGTGATTCGTTTACTTACGCGGTAATGTACAACAATTGAAGAACCAATGTGGGTCGGTGTGGGACGTGTATGGCCTATCGTTCCTCCATTGAGAAGCTCAGGGAATATCTAAAAACAAATCGCCAGTGAGCATTCGATCTCGGAACCTAGAGATCGTATCATATAATAACCTGAGCCCGTGAACGCCTCCTCTTTTGTAGTTATACAAAGAGGATGCGTATCCATGTAAGCGCTCTAGAGGTGGGTCCCCTCGATGGAAACGCTCTATAAAAACGCGTGCCAAATTCAAAGAGGGAAATATAACGTTTGCGAACTGTTTATGACATGCTTCATAAGAGCTTTCAGGGCGGTTCGTCGCATGGCGACGTGTCGGTACGGATCGTTATCGCGTCCTATAGTGAGTAGGACATAGCTTCAATTGTACCCACCTCTGGACGATTGCCTGTACGAACGGGAACATGCA"
    RNA = ""

    #Develop forloop to build RNA string that doesn't add T, but adds U instead
    for i in DNA:
        if i == "T":
            RNA += "U"
        else:
            RNA += i
    
    print "DNA: " + DNA
    print "RNA: " + RNA

main()