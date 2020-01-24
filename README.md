# Simple_ipaddress_hashing

#########################################HOW TO MASK A SINGLE FILE############################################

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing>type logfile
This is my ip address:192.168.0.1
This is my mac 00:1B:44:11:3A:B7
00:1B:44:11:3A:B7,192.168.0.1:8080


D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing>python masking.py logfile logfile-clean

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing>type logfile-clean
This is my ip address:bjc.bgi.a.b
This is my mac 00:1B:44:11:3A:B7
00:1B:44:11:3A:B7,bjc.bgi.a.b:8080

#########################################HOW TO MASK A RECURSIVELY A FOLDER OF LOGS RECURSIVELY############################################

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing>dir
 Volume in drive D is Data
 Volume Serial Number is 9652-C650

 Directory of D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing

24/01/2020  12:11    <DIR>          .
24/01/2020  12:11    <DIR>          ..
24/01/2020  12:11    <DIR>          .idea
24/01/2020  12:11    <DIR>          folder
24/01/2020  11:58             3,255 masking.py
               1 File(s)          3,255 bytes
               4 Dir(s)   8,706,777,088 bytes free

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing>cd folder

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder>dir
 Volume in drive D is Data
 Volume Serial Number is 9652-C650

 Directory of D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder

24/01/2020  12:11    <DIR>          .
24/01/2020  12:11    <DIR>          ..
24/01/2020  12:11    <DIR>          innerfolder
               0 File(s)              0 bytes
               3 Dir(s)   8,706,777,088 bytes free

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder>cd innerfolder

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder\innerfolder>dir
 Volume in drive D is Data
 Volume Serial Number is 9652-C650

 Directory of D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder\innerfolder

24/01/2020  12:11    <DIR>          .
24/01/2020  12:11    <DIR>          ..
24/01/2020  12:08               107 logfile
               1 File(s)            107 bytes
               2 Dir(s)   8,706,777,088 bytes free

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder\innerfolder>type logfile
This is my ip address:192.168.0.1
This is my mac 00:1B:44:11:3A:B7
00:1B:44:11:3A:B7,192.168.0.1:8080


D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder\innerfolder>cd ..

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder>cd ..

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing>python masking.py folder folder-clean
Failed! If this is a folder you are trying to mask, remember to use '-R' option

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing>python masking.py -R folder folder-clean

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing>cd folder-clean

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder-clean>dir
 Volume in drive D is Data
 Volume Serial Number is 9652-C650

 Directory of D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder-clean

24/01/2020  12:11    <DIR>          .
24/01/2020  12:11    <DIR>          ..
24/01/2020  12:12    <DIR>          innerfolder
               0 File(s)              0 bytes
               3 Dir(s)   8,706,777,088 bytes free

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder-clean>cd innerfolder

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder-clean\innerfolder>dir
 Volume in drive D is Data
 Volume Serial Number is 9652-C650

 Directory of D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder-clean\innerfolder

24/01/2020  12:12    <DIR>          .
24/01/2020  12:12    <DIR>          ..
24/01/2020  12:12               107 masked-logfile
               1 File(s)            107 bytes
               2 Dir(s)   8,706,777,088 bytes free

D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder-clean\innerfolder>type masked-logfile
This is my ip address:bjc.bgi.a.b
This is my mac 00:1B:44:11:3A:B7
00:1B:44:11:3A:B7,bjc.bgi.a.b:8080


D:\Users\kenrick.ng\PycharmProjects\Simple_ipaddress_hashing\folder-clean\innerfolder>

