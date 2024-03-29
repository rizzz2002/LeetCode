class Solution(object):
    def twoSum(self, nums, target):
        lst=[]
        flag=True
        for i in range (len(nums)):
            if flag:
                for y in range (i+1,len(nums)):
                    if target==nums[i]+nums[y]:
                        lst.append(i)
                        lst.append(y)
                        flag=False
        return lst