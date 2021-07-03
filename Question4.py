n=int
ch=" "
for n in range (2000,3201):
    if n%7==0 and n%5!=0:
        ch=ch+" "+str(n)
print(ch)