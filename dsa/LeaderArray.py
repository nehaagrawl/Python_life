class LeaderArray:
    # You are given an array arr of positive integers. Your task is to find all the leaders in the array.
    # An element is considered a leader if it is greater than or equal to all elements to its right. 
    # The rightmost element is always a leader
    # Input: arr = [16, 17, 4, 3, 5, 2]
    # Output: [17, 5, 2]
    # Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
    def leader(self,arr):
        lenght_arr=len(arr)
        max_a=arr[lenght_arr-1]
        leader_list=[]
        leader_list.append(max_a)
        for i in range(lenght_arr-2,-1,-1):
            if arr[i]>=max_a:
                max_a=arr[i]
                leader_list.append(max_a)
        leader_list.reverse()
        return leader_list
    
if __name__=="__main__":
    arr=[16, 17, 4, 3, 5, 2]
    obj=LeaderArray()
    res=obj.leader(arr)
    print("leader for give arr",res)
