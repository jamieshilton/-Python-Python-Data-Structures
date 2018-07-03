name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()


for line in handle:
    line = line.rstrip()
    if line == "" : continue
    words = line.split()
    if words[0] != "From" : continue
    times = words[5].split(":")
    counts[times[0]] = counts.get(times[0],0) + 1


for k,v in sorted( [ (k,v) for k,v in counts.items() ] ):
    print k,v