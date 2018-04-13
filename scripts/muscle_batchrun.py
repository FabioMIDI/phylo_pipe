## input: folder with multifastas
## output: folder with aligned multifastas (aligned with muscle -- default parameters)
def makedir(path):
    import os
    path = os.path.abspath(path)
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    # grab file list and put in list
    files = [x for x in glob.glob(path.abspath(args.infolder) + "/*")]
    # create output folder
    muscle_path = "./bin/"
    makedir(args.outfolder)
    
    for f in files:
        
        system(" ".join(["%smuscle" %muscle_path,"-in",f,"-out",path.abspath(args.outfolder)+ "/aligned_" + path.basename(f)]))
        
    
    



if __name__ == "__main__":
    from os import path, system, getcwd
    import glob
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--infolder", "-i", help = "input folder of multifastas")
    parser.add_argument("--outfolder", "-o", help = "output folder of aligned multifastas")
    args = parser.parse_args()
    main()
