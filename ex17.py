#exercise 17

#on the cmd line if you use 'echo 'string' > fileName.txt ' and the cat fileName.txt it will create a little file


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying %s to %s." % (from_file, to_file)

#how do i compine these into one line
in_file = open(from_file)
indata = in_file.read()

print "\n The file you are attempting to copy is %d bytes." % len(indata)

print "\n Does the output file really exist? %r" % exists(to_file)

print "\n If you're ready, hit RETURN, if not, hit ctrl + c."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print """

 Alrighty then, that's a wrap!
"""
out_file.close()
in_file.close()






