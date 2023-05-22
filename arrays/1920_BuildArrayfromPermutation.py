class Solution(object):
    def buildArray(self, nums):
        n = len(nums)
        ans = [0] * n

        for i in range(n):
            ans[i] = nums[nums[i]]

        return ans


# create an instance of the solution class
solution = Solution()

# call the buildArray method and pass the nums parameter
result = solution.buildArray([1,2,0])

print(result)