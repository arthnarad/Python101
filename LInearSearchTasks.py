#Linear Search Task
# 1️ Nearest greater element
def nearest_greater(arr, target):
    greater = None
    for x in arr:
        if x == target:
            return x
        if x > target:
            if greater is None or x < greater:
                greater = x
    return greater if greater is not None else -1


# First and last index
def first_last_index(arr, target):
    first = -1
    last = -1
    for i in range(len(arr)):
        if arr[i] == target:
            if first == -1:
                first = i
            last = i
    return (first, last)


# 3️Count + positions
def count_positions(arr, target):
    count = 0
    pos = []
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1
            pos.append(i)
    return count, pos


# 4️ Closest element index
def closest_index(arr, target):
    min_diff = float('inf')
    idx = -1
    for i in range(len(arr)):
        diff = abs(arr[i] - target)
        if diff < min_diff:
            min_diff = diff
            idx = i
    return idx


# 5️ Mixed data type search
def mixed_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target and type(arr[i]) == type(target):
            indices.append(i)
    return indices


# 6️ List of lists search
def search_2d(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return (i, j)
    return -1


# 7️ Search from both ends
def search_both_ends(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] == target:
            return left
        if arr[right] == target:
            return right
        left += 1
        right -= 1
    return -1


# 8️ First greater & smaller
def greater_smaller(arr, target):
    greater = None
    smaller = None
    for x in arr:
        if x > target:
            if greater is None or x < greater:
                greater = x
        if x < target:
            if smaller is None or x > smaller:
                smaller = x
    return greater, smaller


# 9️ Substring search in list
def substring_search(arr, sub):
    indices = []
    for i in range(len(arr)):
        if sub in arr[i]:
            indices.append(i)
    return indices


# 10 Skip every k-th index
def skip_k_search(arr, target, k):
    for i in range(len(arr)):
        if (i + 1) % k == 0:
            continue
        if arr[i] == target:
            return i
    return -1


# 1️1 Rotated list search
def rotated_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


#  Count comparisons
def search_with_comparisons(arr, target):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == target:
            return i, count
    return -1, count


#  Second occurrence
def second_occurrence(arr, target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1
            if count == 2:
                return i
    return "Not enough occurrences"


# Multiple targets
def multi_search(arr, targets):
    result = {}
    for t in targets:
        result[t] = []
        for i in range(len(arr)):
            if arr[i] == t:
                result[t].append(i)
    return result


#  Longest string
def longest_string(arr):
    longest = ""
    for s in arr:
        if len(s) > len(longest):
            longest = s
    return longest


#  Reverse search
def reverse_search(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1


# Tolerance search ±2
def tolerance_search(arr, target):
    for i in range(len(arr)):
        if abs(arr[i] - target) <= 2:
            return i
    return -1


#  Circular search
def circular_search(arr, target, start):
    n = len(arr)
    i = start
    while True:
        if arr[i] == target:
            return i
        i = (i + 1) % n
        if i == start:
            break
    return -1


#  Max absolute difference
def max_diff_element(arr, target):
    max_diff = -1
    element = None
    for x in arr:
        diff = abs(x - target)
        if diff > max_diff:
            max_diff = diff
            element = x
    return element


#  List of dictionaries search
def dict_search(arr, key, target):
    for i in range(len(arr)):
        if key in arr[i] and arr[i][key] == target:
            return i
    return -1
