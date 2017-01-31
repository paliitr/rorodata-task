import os
import sys

_, filename = os.path.split(sys.argv[1])
name, extension = os.path.splitext(filename)
command = "split {} -l {} {}-part -d --additional-suffix {} --verbose".format(sys.argv[1], sys.argv[2], name, extension)
print("Splitting the file {} to files with {} lines".format(sys.argv[1], sys.argv[2]))
print("Executing the command.")
os.system(command)
print("File splitting finished. If any error occured, please see the output of the split command.")
