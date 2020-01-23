import re
import os
import sys
import string
import shutil
import argparse

def mask_ip(path):
    ip_mapping=dict(zip(range(0,10),string.ascii_lowercase))
    f = open(path, "r")
    nf = open(path + "-sanitised", "w")
    line = f.readline()
    while line:
        wordsInALine = line.split()
        newwords = []
        for word in wordsInALine:
            # check IP address in ipv4 format  and replace them
            if re.search(r"[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*", word):
                match = re.search(r"[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*", word)
                newWordWithIp = []
                print("word is ",word)

                for i in range(match.start(),match.end()):
                    word = list(word)
                    word_original = word[:]
                    try:
                        word[i]=ip_mapping[int(word_original[i])]
                    except:
                        continue
                word = "".join(word)
            # check mac address and replace them
            # word = re.sub(r"[0-9a-zA-Z][0-9a-zA-Z][-:][0-9a-zA-Z][0-9a-zA-Z][-:]"
            #               r"[0-9a-zA-Z][0-9a-zA-Z][-:][0-9a-zA-Z][0-9a-zA-Z][-:]"
            #               r"[0-9a-zA-Z][0-9a-zA-Z][-:][0-9a-zA-Z][0-9a-zA-Z]", "xx:xx:xx:xx:xx:xx", word)
            newwords.append(word)
        newwords = ' '.join(newwords)
        nf.write(newwords + "\n")
        line = f.readline()
    f.close()
    nf.close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Directory to Sanitise')
    parser.add_argument('indir', type=str, help='Input dir for Sanitisation')
    parser.add_argument('outdir', type=str, help='Output dir for Sanitisation')
    args = parser.parse_args()
    shutil.copytree(args.indir,args.outdir)
    for root, dirs, files in os.walk(args.outdir, topdown=True):
        for filename in files:
            fullpath = os.path.join(root,filename)
            mask_ip(fullpath)
            os.remove(fullpath)
