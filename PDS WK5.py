fname = raw_input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
counts = dict()


for line in fh:
    line = line.rstrip()
    if line == "" : continue
    words = line.split()
    if words[0] != "From" : continue
    counts[words[1]] = counts.get(words[1],0) + 1
    

emailcount = None
emailaddress = None
for email,count in counts.items():
    if emailcount < count:
        emailcount = count
        emailaddress = email
print emailaddress, emailcount