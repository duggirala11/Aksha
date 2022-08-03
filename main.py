import re
t="Use py in Ml"
x=re.search("^Use.*M",t)
if(x):
    print("\n\nYes")
else:
    print("\n\n\nno match")

t=" in Use py in Ml in Use py in Ml in Use py in Ml in "
x=re.findall(" ",t)
print(x)

txx = "Bahubali cndj jdcnka;od adcoicnoa;nd edcn;aoads ckijendjc "
searchobj=re.search("\s",txx)