class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di={}
        for i in nums:
            if i not in di:
                di[i]=1
            else:
                di[i]+=1
        freq_elements=sorted(di,key=di.get,reverse=True)
        return freq_elements[:k]
        