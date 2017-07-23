
sort_list=[22,76,24,36,311,54,23,42,16,57,90,73,25,34]


def fast_sort(List,low,high):
    i=low
    j=high

    if i>=j:
        return List

    Key = List[i]

    while i<j:

        while i<j and List[j]>= Key:
            j=j-1

        List[i]=List[j]

        while i<j and List[i]<=Key:
            i=i+1

        List[j]=List[i]
        print(i,j)


    List[i]=Key
        
    fast_sort(List,low, i-1)
    fast_sort(List,j+1,high)

    ##return(List)

fast_sort(sort_list,0,len(sort_list)-1)

print(sort_list)


    
        

        
