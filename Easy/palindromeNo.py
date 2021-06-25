class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        rev=0
        if(num<0):
            #sign="-"
            return False    
        else:
            while(num>0):    
                rem=num%10     
                rev=(rev*10)+rem      
                num//=10                     
            if(rev==x):
                return True
            else:
                return False
