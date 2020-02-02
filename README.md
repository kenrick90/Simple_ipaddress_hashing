# Simple_ipaddress_hashing

Mask logs such that


HOW TO MASK A SINGLE FILE
python masking.py logfile logfile-clean

logfile=logfile to mask
logfile-clean=masked logfile

How to MASK a directory recursively. Every file in the Directory and subdirectory will be masked 
python masking.py -R folder folder-clean

folder=directory to mask
folder-clean=masked directory
