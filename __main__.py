import sys
import hashlib
from usage import usage


def do_check(dictionary, md5_sign):
    with open(str(sys.argv[1])) as f:
        for line in f:
            if hashlib.md5(line.strip('\n').encode('utf-8')).hexdigest() == md5_sign:
                print(line.strip('\n') + "  " + hashlib.md5(line.encode('utf-8')).hexdigest() + "  Passed")
            else:
                print(line.strip('\n') + "  " + hashlib.md5(line.encode('utf-8')).hexdigest() + "  Failed")


if len(sys.argv) < 3:
    usage()
    exit(0)

dict_file = open(str(sys.argv[1]))
md5_file = open(str(sys.argv[2]))
md5_code = md5_file.readline()

do_check(open(str(sys.argv[1])),md5_code)




