import sys
import os

try:
	quastDirectory=sys.argv[1] 
	readsDirectory=sys.argv[2]
	outputDirectory=sys.argv[3]
	pathRefGenone=sys.argv[4] 
except IndexError: 
	print "Invalid input." 
	raise SystemExit

l=os.listdir(readsDirectory) 

files = ""
for item in l:
	item=readsDirectory +"/"+ str(item) + "/contigs.fasta"
	files=files + str(item) + " "
quastDirectory=quastDirectory + "/"

os.system("python %squast.py -o %s -R %s -t 6 %s" % (currentDir, outputDirectory, pathRefGenone, files))

print "The script has finished!"