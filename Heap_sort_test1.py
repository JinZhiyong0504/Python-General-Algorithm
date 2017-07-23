
class Heap_Sort_Ascending():
    Sort_Str = []
    Str_Max_Index = []
    def Heap_Init(self,str):
        self.Sort_Str=str
        self.Str_Max_Index=len(str)-1
        
    def Left_Leaf_Index(self,i):
        return(2*i+1)

    def Right_Leaf_Index(self,i):
        return (2*i+2)

    def Heap_Sort_One_Node(self,k,Maximum_Index):
        
        if k< Maximum_Index:
            Index_Left_Leaf = self.Left_Leaf_Index(k)
            Index_Right_Leaf = self.Right_Leaf_Index(k)            

            print(Index_Left_Leaf,Index_Right_Leaf)

            if Index_Right_Leaf<=Maximum_Index:

                Value_Maximum_Index = k
                
                if self.Sort_Str[k] < self.Sort_Str[Index_Left_Leaf]:
                    Value_Maximum_Index = Index_Left_Leaf
                
                if self.Sort_Str[Value_Maximum_Index]<self.Sort_Str[Index_Right_Leaf]:
                    Value_Maximum_Index = Index_Right_Leaf

                print("Value_Maximum_Index")
                print(Value_Maximum_Index)
                print("k")
                print(k)

                if Value_Maximum_Index != k:
                    print("exchange")
                    self.Sort_Str[Value_Maximum_Index],self.Sort_Str[k] = self.Sort_Str[k],self.Sort_Str[Value_Maximum_Index]
                    self.Heap_Sort_One_Node(Value_Maximum_Index,Maximum_Index)

            elif Index_Right_Leaf> Maximum_Index and Index_Left_Leaf<=Maximum_Index:
                if self.Sort_Str[Index_Left_Leaf] > self.Sort_Str[k]:
                    self.Sort_Str[Index_Left_Leaf],self.Sort_Str[k] = self.Sort_Str[k],self.Sort_Str[Index_Left_Leaf]
            else:
                return ("All children over flow")
            
        
        else:
            return("k is not a reasonable index")

    def Heap_Sort_Tree(self):
        Maximum_Index = self.Str_Max_Index-1
        for i in range(int(Maximum_Index/2)+1,0,-1):            
            self.Heap_Sort_One_Node(i-1,Maximum_Index)
            print(self.Sort_Str)

    def Heap_Sort_Str(self):
        for j in range(self.Str_Max_Index,0,-1):
            if self.Sort_Str[0]>self.Sort_Str[j]:
                self.Sort_Str[0],self.Sort_Str[j] = self.Sort_Str[j],self.Sort_Str[0]
            self.Heap_Sort_One_Node(0,j-1)


    
sort_list=[311,76,24,36,22,54,23,42,16,57,90,73,25,34]
P= Heap_Sort_Ascending()
P.Heap_Init(sort_list)
P.Heap_Sort_Tree()

P.Heap_Sort_Str()
print(P.Sort_Str)
