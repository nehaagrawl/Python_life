# Given an array of integers arr[], the task is to find the first equilibrium point in the array.
# The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it.
# Return -1 if no such point exists. 
# Input: arr[] = [1, 2, 0, 3]
# Output: 2 
# Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.
class Equilibriumpoint:
    def findEquilibrium(str,arr):
        left_sum=0
        right_sum=0
        total=0
        for i in range(len(arr)):
            total+=arr[i]
        
        for j in range(len(arr)):
            right_sum=total-left_sum-arr[j]
            if right_sum==left_sum:
                return j
            left_sum+=arr[j]
        return -1
    
if __name__=="__main__":
    # arr = [2,1,0,3]
    obj=Equilibriumpoint()
    arr = [2,1,0,3]
    equi_index=obj.findEquilibrium(arr)
    print("Equilibriumpoint index (pivot) is",equi_index,"and index value",arr[equi_index])



