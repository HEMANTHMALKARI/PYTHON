num=int(input(""))
rnum=0
while num>0:
    rem=num%10
    rnum=(rnum*10)+rem
    num=num//10
print(rnum)
