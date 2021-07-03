p=int(input("Please type the price"))
d=int
if p<200:
    d=p*10/100
elif p>500:
    d=p*50/100
else:
    d=p*30/100

print("the discounted price is",d)


