
sort_list=[311,76,24,36,22,54,23,42,16,57,90,73,25,34]


def bubble(list):
    list_len = len(list)

    while list_len >=0:

        for i in range(list_len-1):

            if sort_list[i] > sort_list[i+1]:
                m=sort_list[i]
                sort_list[i] = sort_list[i+1]
                sort_list[i+1] = m

        list_len = list_len -1
    
    


bubble(sort_list)

print(sort_list)
                
            
        
    
