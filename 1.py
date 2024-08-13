num=int(input())
f=0
for i in range(2,num//2+1):
    if num%i==0:
        f=1
        break
if f==1:
    print("not prime")
else:
    print("prime")
