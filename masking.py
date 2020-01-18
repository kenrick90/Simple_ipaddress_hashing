import re
import string
import sys
if __name__=='__main__':
    if len(sys.argv) == 1:
        print "You can also give filename as a command line argument"
        filename = raw_input("Enter Filename: ")
    else:
        filename = sys.argv[1]
    ip_mapping=dict(zip(range(0,10),string.ascii_lowercase))
    try:
        f = open(filename,"r")
    except:
        print "No such file or no permissions"
        exit()
    nf= open(filename + ".sanitised","w")
    line = f.readline()
    while line:
        words = line.split()
        newwords=[]
        for word in words:
            #check IP address in ipv4 format  and replace them
            if re.match(r".*[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*",word):
                wordWithIp = []
                for c in word:
                    try:
                        c = int(c)
                        c = ip_mapping[c]
                    except:
                        c = c
                    wordWithIp.append(c)
                    word=''.join(wordWithIp)
            #check mac address and replace them
            word=re.sub(r"[0-9a-zA-Z][0-9a-zA-Z][-:][0-9a-zA-Z][0-9a-zA-Z][-:]"
                    r"[0-9a-zA-Z][0-9a-zA-Z][-:][0-9a-zA-Z][0-9a-zA-Z][-:]"
                    r"[0-9a-zA-Z][0-9a-zA-Z][-:][0-9a-zA-Z][0-9a-zA-Z]","xx:xx:xx:xx:xx:xx",word)
            newwords.append(word)
        newwords = ' '.join(newwords)
        nf.write(newwords+"\n")
        line = f.readline()
    f.close()
    nf.close()
    print str(nf) + " file written"


