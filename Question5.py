n=int(input("PLease type a number"))
f=1
for i in range (1,n+1):
    f=f*i
if n==0:
    f=1
print("the factorial of this number is",f)