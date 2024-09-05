def count(arr,exp):
    size=len(arr)
    cli=[0]*10
    op=[0]*size
    for i in arr:
        index=i//exp
        cli[index%10]+=1
    for i in range(1,len(cli)):
        cli[i]+=cli[i-1]
    i=size-1
    while(i>=0):
        index=arr[i]//exp
        op[cli[index%10]-1]=arr[i]
        cli[index%10]-=1
        i-=1
    for i in range(size):
        arr[i]=op[i]
    print(arr)
def radix(arr):
    exp=1
    max1=max(arr)
    while(max1/exp>1):
         count(arr,exp)
         exp=exp*10
radix([170,45,75,90,802,24,2,65])
