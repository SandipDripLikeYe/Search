n=111001101
srg=str(n)
l=len(srg)
res=""
sum=0
for i in range(0,l):

    if srg[i]=="1":
        sum=sum+1
        if i<l-1:
            if srg[i+1]=="0":
                res=res+str(sum)
    else:
        sum=0
        res=res+str(sum)
res=res+str(sum)
print(res)
        
