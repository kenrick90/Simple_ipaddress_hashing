import re
import os
import string
import shutil
import argparse
def mask_ip(inFile, outFile, macAddress):
    #This is the mapping if the ip digits to alphabets, 0 -> 'a' , 1 -> 'b' ...
    ip_mapping=dict(zip(range(0,10),string.ascii_lowercase))
    f = open(inFile, "r")
    nf = open(outFile, "w")
    line = f.readline()
    while line:
        # check IP address in ipv4 format  and replace them
        if re.search(r"[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*", line):
            matchlist = re.findall(r"[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*", line)
            for match in matchlist:
                m = re.search(match, line)
                #Only tweak the characters which are the IP address and not other parts of the line
                for i in range(m.start(),m.end()):
                    line = list(line)
                    line_original = line[:]
                    try:
                        line[i]=ip_mapping[int(line_original[i])]
                    except:
                        continue
                line = "".join(line)
        # check mac address and replace them
        if macAddress == True:
            line = re.sub(r"[0-9a-zA-Z][0-9a-zA-Z][-:][0-9a-zA-Z][0-9a-zA-Z][-:]"
                          r"[0-9a-zA-Z][0-9a-zA-Z][-:][0-9a-zA-Z][0-9a-zA-Z][-:]"
                          r"[0-9a-zA-Z][0-9a-zA-Z][-:][0-9a-zA-Z][0-9a-zA-Z]", "xx:xx:xx:xx:xx:xx", line)
        nf.write(line)
        line = f.readline()
    f.close()
    nf.close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Mask IP address of input file by writing a output file with the IP address changed')
    parser.add_argument('-R', '--recursive', action='store_true',
                        help="recursively sanitised entire directory and its files")
    parser.add_argument('-m', '--macAddress', action='store_true',
                        help="If enabled, mask mac address into xx:xx:xx:xx:xx:xx, default is not enabled")
    parser.add_argument('input',type=str, help='Input directory OR file for masking')
    parser.add_argument('output',type=str, help='Output directory or file for masking')
    args = parser.parse_args()

    #create a separate folder for this tasks
    if args.recursive:
        try:
            shutil.copytree(args.input,args.output)
        except:
            print "Output directory already exist or no permission! Please try again with another " \
                  "output directory name or delete existing output directory folder."
            quit()
        for root, dirs, files in os.walk(args.output, topdown=True):
            for filename in files:
                filepath = os.path.join(root, filename)
                newfilepath = os.path.join(root,"masked-"+filename)
                mask_ip(filepath,newfilepath,args.macAddress)
                os.remove(filepath)
        quit()
    mask_ip(args.input, args.output, args.macAddress)

