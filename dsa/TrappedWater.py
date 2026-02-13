class TrappedWater:
    # Given an array arr[] with non-negative integers representing the height of blocks. 
    # If the width of each block is 1, 
    # compute how much water can be trapped between the blocks during the rainy season.  [3, 0, 2, 0, 4] res=7
    def maxWater(self,arr):

        res=0
        for i in range(1,len(arr)-1):
            lmax=arr[i]
            for j in range(i):
                lmax=max(lmax,arr[j])
            rmax=arr[i]
            for j in range(i+1,len(arr)):
                rmax=max(rmax,arr[j])
            res += min(lmax,rmax)-arr[i]
        return res
    
obj=TrappedWater()
arr= [3, 0, 2, 0, 4]
print(obj.maxWater(arr))

            


