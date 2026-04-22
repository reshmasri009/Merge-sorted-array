def merge(nums1, m, nums2, n):
    p1 = m - 1  
    p2 = n - 1  
    p = m + n - 1  
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

    return nums1
m = int(input("Enter number of valid elements in nums1 (m): "))
n = int(input("Enter number of elements in nums2 (n): "))

print("Enter nums1 elements (with extra 0s at the end):")
nums1 = list(map(int, input().split()))

print("Enter nums2 elements:")
nums2 = list(map(int, input().split()))

print("Before merge:", nums1)
result = merge(nums1, m, nums2, n)
print("After merge:",result)
