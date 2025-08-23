weight = [1,2,4,5]
val = [5,4,8,6]

max_weight = 5

def knapsack(weight,val,max_weight):
    results = []
    def backtrack(indx,current_weight,path):
        
        if indx >= len(weight):
            if current_weight <= max_weight:
                results.append(path[:]) 
            return
        
        path.append(val[indx])
        backtrack(indx+1,current_weight+weight[indx],path)
        path.pop()
        
        backtrack(indx+1,current_weight,path)
    backtrack(0,0,[])
    return results
    
print(knapsack(weight,val,max_weight))
