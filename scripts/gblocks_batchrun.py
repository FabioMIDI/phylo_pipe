def cleanup(mypath,ext):
    import os
    import shutil
    for e in ext:
        to_remove = [x for x in glob.glob("{}/*{}".format(os.path.abspath(mypath) ,e))]
        for i in to_remove:
            try:
                os.remove(i)    
            except OSError:
                shutil.rmtree(i, ignore_errors=True)

def makedir(path):
    import os
    path = os.path.abspath(path)
    if not os.path.exists(path):
        os.makedirs(path)
        
        
def main(): 
    gblocks_path = "./bin/"
    for f in glob.glob(path.abspath(args.infolder) + "/*"):
    #Gblocks Mguil_catenated_aln.faa -d=y
        system("%sGblocks %s -d=y" %(gblocks_path,f))
    cleanup(args.infolder,[".htm","-gbPS"])
    # copy files
    makedir(args.out)
    for f in glob.glob(path.abspath(args.infolder) + "/*gb"):
        move(f, path.abspath(args.out) + "/" + path.basename(f))
    

    
    
    
    
    
    
    
if __name__ == "__main__":    
    import argparse
    import glob
    from shutil import move 
    from os import system, path, remove, stat
    parser = argparse.ArgumentParser()
    parser.add_argument("--infolder", "-i", help = "aligned phi-tested multifasta folder") #only alignments in here plz
    parser.add_argument("--out", "-o", help = "output folder") #
    args = parser.parse_args()
    main()
