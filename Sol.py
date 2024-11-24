def twoSum(nums, target):
        i=0 
        j=len(nums)-1 
        while i<j:
            sum=nums[i]+nums[j]
            if sum==target:
                return [i,j]
                break 
            elif sum<target:
                i+=1 
            else:
                j-=1        
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))
        
