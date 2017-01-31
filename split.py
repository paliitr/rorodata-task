import os
import sys

command = "split {} -l {} {}-part -d".format(sys.argv[1], sys.argv[2], sys.argv[1].split(".")[-2])
os.system(command)
