parent = "abcdabc"
child = "abc"



def subsets(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])

# subsets(parent)

def str_match_naive(parent,child):
    len_child = len(child)
    results = []
    
    if len(parent) == 0 and len(child) == 0:
    return True
    
    if(len(parent)<len_child):
        return False
    
    elif(len(parent) == len(child) and parent == child):
        return True
    
    for i in range(0,(len(parent)-len(child))+1):
        print(f"I:{i},...{parent[i: i+len(child)]}")
        if(parent[i:i+len(child)] == child):
            # return (f"start:{i} stop:{i+len(child)-1}")
            results.append((i,i+len(child)-1))
    
    if results:
        return results
        
    return False
        
    
    
def str_match(parent,child):
    if(len(parent)<len(child)):
        return -1
        
    if(len(parent) == len(child) and parent == child):
        return (f"0 : {len(parent)}")
        
    for i in range(len(parent)):
        if(parent[i] == child[0]):
            for j in range(i,len(parent)):
                if(parent[i:j+1] == child):
                    return (f"i:{i},j:{j}")
                    
    return -1
 



print(str_match_naive(parent,child))