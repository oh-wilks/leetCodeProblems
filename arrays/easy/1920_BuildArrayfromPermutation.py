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

array = [0,2,1,5,3,4]
n = len(array)
ans = [0] * n
print(f"array lenght {n}")
print(f"empty array {ans}")
for i in range(n):
    ans[i] = array[array[i]]
print(array)
print(ans)

array = [5,0,1,2,3,4]
n = len(array)
ans = [0] * n
print(f"array lenght {n}")
print(f"empty array {ans}")
for i in range(n):
    ans[i] = array[array[i]]
print(array)
print(ans)