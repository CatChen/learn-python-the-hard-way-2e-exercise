from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
input_file = open(from_file)
indata = input_file.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

output_file = open(to_file, 'w')
output_file.write(indata)

print("Alright, all done.")

output_file.close()
input_file.close()
