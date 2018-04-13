# input: a folder with aligned (protein) multifastas
# output: a concatenated multifasta of alignments (used for phylogenetic analyses)
def main():
    aligned = glob.glob(path.abspath(args.aln) + "/*" )
    # initialize dictionary of sequences with keys:
    cat = {k:"" for k in SeqIO.to_dict(SeqIO.parse(aligned[0], "fasta")).keys()}
    # loop to fill the others
    for a in aligned:
        d = SeqIO.to_dict(SeqIO.parse(a, "fasta"))
        for k in d.keys():
            cat[k] += str(d[k].seq)
    outfile = open(path.abspath(args.out), "w")
    for k in cat.keys():
        outfile.write(">" + k + "\n")
        outfile.write(cat[k] + "\n")
    outfile.close()
        
    




if __name__ == "__main__":
    import argparse
    from Bio import SeqIO
    import glob
    from os import path, system, makedirs
    parser = argparse.ArgumentParser()
    parser.add_argument("--aln", "-a", help = "aligned proteins folder")    #only aligned proteins should be in this folder
    parser.add_argument("--out", "-o", help = "outfile path")
    args = parser.parse_args()
    main()
    
