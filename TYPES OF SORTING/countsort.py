def countsort(arr):
    size=len(arr)
    count_list=[0]*(max(arr)+1)
    output_list=[0]*size
    for i in arr:
        count_list[i]+=1
    for i in range(1,len(count_list)):
        count_list[i]+=count_list[i-1]
    i=size-1
    while(i>=0):
        output_list[count_list[arr[i]]-i]=arr[i]
        count_list[arr[i]]-=1
        i-=1
    for i in range(size):
        arr[i]=output_list
    print(arr)
countsort([2,2,1,1,10,10,11,0])
        
