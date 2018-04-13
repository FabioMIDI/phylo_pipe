def main():

    fasta_folder = os.path.abspath(args.infolder)
    number_threads = args.threads
    remove_temp = args.remove_temp

    bin_path = "bin/"

# Ricerca degli ortologhi
    os.system("%sorthofinder -f %s -t %s -og" % (bin_path, fasta_folder, number_threads))

    ortho_results = glob(fasta_folder + "/Results*" )[0]
    ortho_csv = ortho_results + "/Orthogroups.csv"
    script_path = "scripts/"
    read_ortho_out = fasta_folder + "/read_ortho_out"

# Isolamento degli ortologhi in singola copia
    os.system("python %sread_ortho_out.py -i %s -p %s -o %s" % (script_path, ortho_csv, fasta_folder, read_ortho_out))

    single_copy = read_ortho_out + "/single_copy_orthogroups"
    muscle_out = fasta_folder + "/muscle_out"

# Multiallineamento degli ortologhi in singola copia
    os.system("python %smuscle_batchrun.py -i %s -o %s" % (script_path, single_copy, muscle_out))

# Test di Phi [opzionale]
    if args.phi == True:
        phi_out = fasta_folder + "/phi_out"
        os.system("python %sphi_batchrun.py -i %s -o %s" % (script_path, muscle_out, phi_out))
        if os.listdir(phi_out) == []:
            print "You don't have enough taxa for running Phi"
            phi_out = muscle_out
    elif args.phi == False:
        phi_out = muscle_out

    gblock_out = fasta_folder + "/gblock_out"

# Gblocks
    os.system("python %sgblocks_batchrun.py -i %s -o %s" %(script_path, phi_out, gblock_out))

    orthos2cat_out = fasta_folder + "/orthos2cat_out"

# Concantenazione degli allineamenti ottenuti
    os.system("python %sorthos2cat.py -a %s -o %s" %(script_path, gblock_out, orthos2cat_out))

# cartella temp [opzionale]
    temp = fasta_folder + ("/temp")

    if os.path.exists(temp) == False:
        os.mkdir(temp)
    else:
        temp_list = glob(fasta_folder + "/temp*")
        temp_list = [x.replace(fasta_folder+"/","") for x in temp_list]
        print temp_list
        if len(temp_list) == 1:
            new_temp = temp + "_1"
        else:
            temp_list.remove("temp")
            temp_list = [int(x.split("_")[1]) for x in temp_list]
            temp_list.sort()
            new_temp = "temp_" + str(temp_list[-1] + 1)
            new_temp = fasta_folder + "/" + new_temp
        os.mkdir(new_temp)
        temp = new_temp

# Trasferimento degli output nella cartella temp
    os.system("mv %s %s" %(ortho_results, temp))
    os.system("mv %s %s" %(read_ortho_out, temp))
    os.system("mv %s %s" %(muscle_out, temp))
    os.system("mv %s %s" %(phi_out, temp))
    os.system("mv %s %s" %(gblock_out, temp))
    os.system("cp %s %s" %(orthos2cat_out, temp))

    if remove_temp == True:
        shutil.rmtree(temp)

if __name__ == "__main__":
    import os
    from glob import glob
    import shutil
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--infolder", "-i", help = "input folder of multifastas")
    parser.add_argument("--threads", "-t", type = int, help = "number of threads")
    parser.add_argument("--remove_temp", "-r", type = bool, default = False, help = "remove temp folder")
    parser.add_argument("--phi", "-p", type = bool, default = False, help = "run Phi test - default False")
    args = parser.parse_args()
    main()
