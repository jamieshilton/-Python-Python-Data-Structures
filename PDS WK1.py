text = "X-DSPAM-Confidence:    0.8475"
pos = text.find("0")
end = len(text)
toprint = text[pos:end]

print float(toprint)