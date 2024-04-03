class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        index=len(x)-1
        for i in range (len(x)):
            for y in range (index,-1,-1):
                if x[i]==x[y]:
                    index-=1
                    break
                else:
                    return False
        return True