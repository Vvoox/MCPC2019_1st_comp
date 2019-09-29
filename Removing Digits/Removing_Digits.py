count = 0
ipt = int(input())
while(ipt!=0):
   tab=[int(i) for i in str(ipt)]
   ipt = ipt - max(tab)
   count+=1
print(count)