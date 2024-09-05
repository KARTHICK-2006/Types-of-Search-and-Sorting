a=[8,5,7,6,4]
n=len(a)
for i in range(0,n):
    c=0
    for j in range(0,n-i-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
            c=1
    if c!=1:
        break
print(a)
