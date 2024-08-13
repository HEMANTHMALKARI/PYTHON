a=input("")
b=list(map(int,a.split()))
#print(max(bls))
max=b[0]
for i in b:
    if i>max:
        max=i
print(max)
