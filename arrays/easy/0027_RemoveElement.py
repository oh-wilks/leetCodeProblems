
def remove_element(nums, val):
    k = 0  # Number of elements not equal to val
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

# Example 1
nums1 = [3, 2, 2, 3]
val1 = 3
expectedNums1 = [2, 2]
expectedLength1 = len(expectedNums1)

k1 = remove_element(nums1, val1)
print(k1)


# Example 2
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
expectedNums2 = [0, 0, 1, 3, 4]
expectedLength2 = len(expectedNums2)

k2 = remove_element(nums2, val2)
print(k2)