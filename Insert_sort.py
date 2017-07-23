
sort_list=[311,76,24,36,22,54,23,42,16,57,90,73,25,34]


def insert_sort(list):

    for i in range(len(list)):
        Maximum=i
        for j in range(i+1,len(list),1):
            if list[j]<list[Maximum]:
                Maximum = j

        if Maximum != i:
            tmp = list[i]
            list[i] = list[Maximum]
            list[Maximum] = tmp


    print(list)
                
            
insert_sort(sort_list)
    
