string = 'X-DSPAM-Confidence:0.8475'
ind=string.find(":")
val=float(string[ind+1:])
print(val)
