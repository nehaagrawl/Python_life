class LargestElement:

    def arrays(__init__,arr):
        max=arr[0]
        for i in arr[1:]:
            print(i)
            # print(arr[i])
            if i>max:
                max=i
        return max
    
obj=LargestElement()
arr=[12,3,45,53335,234,2,1,9]
print("largest element of array: ",obj.arrays(arr))