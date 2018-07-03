fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	line = line.rstrip().split()
	for w in line:
		if w in lst:
			continue
		else:
			lst.append(w)
lst.sort()
print lst