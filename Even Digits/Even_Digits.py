cpt = 0
mylist = [0]
y=input()
x = [int(i) for i in input().split()]
if (len(x)==int(y)):
    x = list(dict.fromkeys(x))
    for i in x :
        if (i%2==0):
            cpt=cpt+1
print(cpt)