# Two-Pointer-Approach

The Two Pointer Approach is a common algorithmic technique used to solve problems efficiently by maintaining two pointers (or indices) to traverse the data structure. This technique is particularly effective for problems involving arrays or linked lists, especially when the input is sorted or partially sorted. It helps reduce the time complexity by avoiding nested loops.

Key Idea
Use two pointers to scan or process the data in tandem, often in opposite directions or from a specific starting position.
Depending on the problem, pointers are moved based on a condition (e.g., sum comparison, target match, or duplicates removal).
Common Use Cases
Finding pairs with a given sum in a sorted array.
Removing duplicates in sorted arrays.
Reversing parts of an array or string.
Merging two sorted arrays.
Sliding window problems.
Example Problems
1. Two Sum in Sorted Array
Find two numbers in a sorted array that sum up to a given target.

Approach:
Use two pointers: one starting from the beginning (left) and one from the end (right).
Compare the sum of the elements at the two pointers with the target:
If the sum is less than the target, move the left pointer forward.
If the sum is greater than the target, move the right pointer backward.
If the sum matches the target, return the pair.
Implementation:
python
Copy code
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

# Example
arr = [1, 2, 3, 4, 6]
target = 6
print(two_sum_sorted(arr, target))  # Output: (2, 4)
2. Removing Duplicates in a Sorted Array
Remove duplicates in-place from a sorted array and return the new length.

Approach:
Use one pointer (slow) to maintain the position of the unique elements.
Use another pointer (fast) to scan the array.
When arr[fast] is different from arr[slow], increment slow and update arr[slow].
Implementation:
python
Copy code
def remove_duplicates(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1

# Example
arr = [1, 1, 2, 2, 3, 4, 4]
length = remove_duplicates(arr)
print(arr[:length])  # Output: [1, 2, 3, 4]
3. Container with Most Water
Find the maximum area that can be formed between two lines (indices represent heights).

Approach:
Use two pointers (left and right) at the start and end of the array.
Calculate the area formed by the lines at left and right:
Move the pointer corresponding to the shorter line inward.
Keep track of the maximum area.
Implementation:
python
Copy code
def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        width = right - left
        current_area = width * min(height[left], height[right])
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# Example
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))  # Output: 49
Benefits
Efficient: Reduces the need for nested loops, improving time complexity (often 
𝑂
(
𝑛
)
O(n)).
Simple: Intuitive to implement once you identify the correct conditions for pointer movement.
Space-saving: Operates in 
𝑂
(
1
)
O(1) space for most problems.
Limitations
Typically works well for problems with sorted data or linear structures.
Requires careful handling of edge cases (e.g., empty input or special conditions).
Let me know if you need examples for specific types of problems using this approach!
