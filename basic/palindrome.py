class Solution:
    def isPalindrome(self, n):
       # s=str(n)
       # return s==s[::-1]
        
        rev=0
        original=n
        
        if n < 0:
            return false
            
        while n > 0:
            rev=rev*10+(n%10)
            
            n//=10
            #print(rev)
        return rev==original
    
obj=Solution()
print(obj.isPalindrome(535))