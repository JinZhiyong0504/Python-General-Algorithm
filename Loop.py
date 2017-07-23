
sort_list=[311,22,54,23,42,16,57,90]

#def insert_sort(sort_list):
len_list = len(sort_list)

k=1;    
if len_list >=1:
    for i in range(0,len_list):
        j = i+1
        
        while j<len_list:
            if sort_list[j]<sort_list[i]:
                key = sort_list[i]
                sort_list[i] = sort_list[j]
                sort_list[j] = key                
            j = j + 1

print(len_list)

print(sort_list)
