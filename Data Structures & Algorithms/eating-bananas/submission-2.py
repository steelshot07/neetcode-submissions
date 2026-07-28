class Solution:
    def hour(self,arr:List[int], hourly: int)-> int:
        totalHours = 0
        for i in range(0, len(arr)):
            totalHours += math.ceil(arr[i]/hourly)
        return totalHours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        while low<=high:
            mid = (high+low)//2
            totalHours = self.hour(piles,mid)
            if totalHours<=h:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        
        return ans
