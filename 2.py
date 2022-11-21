g1=input()
g2=input()
l=list(g1)
count=0
n=g2[len(g2)-1]
for i in l:
    if n in i:
        count+=1
print(count)