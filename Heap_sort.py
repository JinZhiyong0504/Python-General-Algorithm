
class Max_Heap_Sort(object):

    list_sort = []
    heap_Max_Index = 0

    def _init_(self,list_raw):
        ##print(list_raw)
        self.list_sort = list_raw
        self.heap_Max_Index = len(self.list_sort)-1
    
    def left_leaf(self,i):
        return (2*i+1)

    def right_leaf(self,i):
        return (2*i+2)

    def parent(self,i):
        if i%2 == 1:
            return(int(i/2))
        else:
            return(i/2-1)

    def Max_Parent(self, i, Search_Max_Index):

        if Search_Max_Index is None:
            return list

        l = self.left_leaf(i)
        r = self.right_leaf(i)
        ##print(l,r)
            
        if r <= Search_Max_Index:            
            max_index = i
            if self.list_sort[i] < self.list_sort[l]:
                max_index = l                
            if self.list_sort[max_index] < self.list_sort[r]:
                max_index = r            
            if max_index !=i:                
                self.list_sort[i],self.list_sort[max_index] = self.list_sort[max_index],self.list_sort[i]
                self.Max_Parent(max_index,Search_Max_Index)
        elif r> Search_Max_Index and l<= Search_Max_Index:
            if self.list_sort[i]< self.list_sort[l]:
                self.list_sort[i],self.list_sort[l] = self.list_sort[l],self.list_sort[i]
     
        ##print(self.list_sort)

    def Max_Heap_Setup(self,Maxmum_Index):
        #print(length)        
        for i in range(int(Maxmum_Index/2)+1):
            self.Max_Parent(int(Maxmum_Index/2)+1-i,Maxmum_Index)
            
    def Heap_Max_Sort(self):
        List_Max_Index = len(self.list_sort)-1
        for i in range(len(self.list_sort)):
            if self.list_sort[0]>self.list_sort[List_Max_Index-i]:
                self.list_sort[0],self.list_sort[List_Max_Index-i] = self.list_sort[List_Max_Index-i],self.list_sort[0]
            self.Max_Parent(0,List_Max_Index-i-1)


sort_list=[311,22,54,23,42,16,57,90,73,25,34]

P = Max_Heap_Sort()


P._init_(sort_list)

##print(P.heap_length)
P.Max_Heap_Setup(P.heap_Max_Index)


P.Heap_Max_Sort()

print(P.list_sort)
