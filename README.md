# Merge-sorted-array
merging sorted array using three pointers
#Algorithm:
-take 3 pointers p1,p2,p where p1 reads from last element in nums1 last element in nums2 and last index of nums1 respectively
-compare the elements from back and place the larger at p
-continue until one array is completed
-if nums1 has left some elements copy them into nums1
#Complexity:
time=O(m+n)
space=O(1)
