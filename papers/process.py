import sys,re,os,msvcrt

if len(sys.argv) != 4:
	print ("usage: process.py <input_file> <opcode> <oprand>")
	print ("       operations: sort a/s")
	print ("                   query <word>")
	print ("                   review f/r")
	print ("                   interact f/r")
	exit()

opcode = sys.argv[2]
oprand = sys.argv[3]
input_file = sys.argv[1]

if opcode != "sort" and opcode != "query" and opcode != "review" and opcode != "interact":
	print ("wrong opcode")
	exit()
if (opcode == "sort" and (oprand != "a" and oprand != "s")):
	print ("wrong oprand")
	exit()
if (opcode == "review" and (oprand != "f" and oprand != "r")):
	print ("wrong oprand")
	exit()
if (opcode == "interact" and (oprand != "f" and oprand != "r")):
	print ("wrong oprand")
	exit()
if not os.path.exists(input_file):
	print ("no such file")
	exit()
	
fp = open(input_file, 'r')

text = []
for ln in fp.readlines():
	if ln != "\n":
		text.append(ln.strip('\n'))

if opcode == "query":
	for line in text:
		line.strip('\n')
		if re.search(oprand, line):
			print line

elif opcode == "sort":
	if oprand == "a":
		text.sort()
		for line in text:
			print line
	elif oprand == "s":
		if len(text[0].split('|')) == 2:
			i = 1
			for line in text:
				print (line.split('|')[0] + " | " + line.split('|')[1] + " | " + str(i).zfill(4))
				i = i+1
		elif len(text[0].split('|')) == 3:
			for line in sorted(text, key=lambda line : line.split('|')[2] ):
				print line
		
elif opcode == "review":
	if oprand == "f":
		for line in text:
			line.strip('\n')
			print line.split('|')[0]
	elif oprand == "r":
		for line in text:
			line.strip('\n')
			print line.split('|', 1)[1]
elif opcode == "interact":
	if oprand == "f":
		for line in text:
			line.strip('\n')
			print line.split('|')[0],
			msvcrt.getch()
			print line.split('|', 1)[1]
			msvcrt.getch()
	elif oprand == "r":
		for line in text:
			line.strip('\n')
			print line.split('|', 1)[1],
			msvcrt.getch()
			print line.split('|')[0]
			msvcrt.getch()