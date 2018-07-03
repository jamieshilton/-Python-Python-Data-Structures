# Use the file name mbox-short.txt as the file name
sum_spam = 0
spam_count = 0

fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()    
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sum_spam = sum_spam + float(line[20:26])
    spam_count = spam_count + 1
print "Average spam confidence:",sum_spam / spam_count