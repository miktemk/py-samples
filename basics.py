import sys, os, re
import time, datetime
import getopt

# command line options: note the first line parameter and the if statements below
optlist, args = getopt.getopt(sys.argv[1:], "d:m:o:")
#print optlist
opt_d = 8000
opt_m = "none"
opt_o = None
for opt,arg in optlist:
	if opt == "-d":
		opt_d = int(arg)
	if opt == "-m":
		opt_m = arg
	if opt == "-o":
		opt_o = arg

# list dir
dirname = "."
dirList = os.listdir(dirname)
for fname in dirList:
	if fname == os.path.basename(__file__):
		continue
	if fname == "ZZZrun.bat":
		continue
	fullPath = dirname + "\\" + fname
	if os.path.isdir(fullPath):
		print("dir", fullPath)
	else:
		print("file", fullPath)

# read file lines
fname = "file.txt"
if os.path.exists(fname):
	infile = open(fname)
	text = infile.read()
	#lines = infile.readlines() ### or read everything into array of lines
	infile.close()

# write to file
fff = open("log.txt", "w")	
fff.write("""
shieeeet
""")
fff.close()

# datetime, int padding, date label
today = datetime.date.today()
month = str(today.month).zfill(2)
day = str(today.day).zfill(2)
dateLabel = `today.year` + "_" + month + "_" + day
print("today", dateLabel)

# stdin
inputShit = input("raw_input test: ")
print(inputShit)

#output dir
OUT_DIR = "output_dir"
outdir = dirname + "/" + OUT_DIR
if not os.path.exists(outdir):
	os.mkdir(outdir)






#------------- other -------------
# to concat 2 binary files
#destination = open(outfile,'wb')
#shutil.copyfileobj(open(file1,'rb'), destination)
#shutil.copyfileobj(open(file2,'rb'), destination)
#destination.close()
