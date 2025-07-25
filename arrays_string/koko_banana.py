import math
class Solution:

    def check_k(self,piles,k,deadline):
        time = 0
        for i in range(len(piles)):
            time += math.ceil(piles[i] / k)
        if(time>deadline):
            return -1
        elif(time<=deadline):
            return 1
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def custom_bs(piles,deadline):
            low = 1
            high = max(piles)
            k = high
            
            while(low<=high):
                mid = (high+low)//2
                temp = self.check_k(piles,mid,deadline)
                if(temp == -1):
                    low = mid+1
                if(temp == 1):
                    k = mid
                    high = mid - 1
                    
            return k
        return custom_bs(piles,h)