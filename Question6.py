ch=str(input("Please type one or more words"))
evn=" "
for i in range (0,len(ch)):
    if i%2==0:
        evn=evn+ch[i]
print(evn)