# p-value has to be greater than 0.05 in all tests, 1k permutations
def makedir(path):
    import os
    path = os.path.abspath(path)
    if not os.path.exists(path):
        os.makedirs(path)




def main():
    files = glob.glob(path.abspath(args.infolder) + "/*")
    t = 0
    makedir(args.out)
    phi_path = "./bin/"
    print files
    print getcwd()
    for f in files:
        t += 1
        # run Phi with all tests and 1k permutations
        system(" ".join([ "%sPhi" % phi_path, "-f",f,"-t","A", "-p","1000","-o",">","output.phi","2>", "error.phi"]))
        # check error log, if empty continue
        if stat("error.phi").st_size == 0:
            # extract results from output
            system(" ".join(["egrep", "\"(Max Chi\^2|NSS:|PHI \(Permutation)\"", "output.phi", ">", "tests.phi"  ]) )
            # parse results
            o = [1 if float(l.split(":")[1].split("(")[0].lstrip().rstrip()) > 0.05 else 0 for l in open("tests.phi","r")]
            for g in ["tests.phi", "output.phi"]:
                remove(g)
            if sum(o) == 3:
                print f, args.out
                copyfile(f, path.abspath(args.out) + "/" + path.basename(f) +"norec")

    for x in ["Phi.log","Phi.inf.list","Phi.inf.sites", "Phi.poly.unambig.sites", "error.phi"]:
        remove(x)


            
        
        
    
    
    



if __name__ == "__main__":    
    import argparse
    import glob
    from shutil import copyfile 
    from os import system, path, remove, stat, getcwd
    parser = argparse.ArgumentParser()
    parser.add_argument("--infolder", "-i", help = "aligned multifasta folder") #only alignments in here plz
    parser.add_argument("--out", "-o", help = "output folder") #
    args = parser.parse_args()
    main()
