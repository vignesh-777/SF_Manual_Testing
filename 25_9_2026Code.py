#------------------------------------------------------------------------------#
# 1. STUDENT ATTENDANCE ANALYSIS
# Longest continuous sequence without duplicate student IDs

def AttendanceAnalysis(lst):

    seen = set()
    left = 0
    longest_seq = []

    for right in range(len(lst)):

        while lst[right] in seen:
            seen.remove(lst[left])
            left += 1

        seen.add(lst[right])

        if right - left + 1 > len(longest_seq):
            longest_seq = lst[left:right + 1]

    return longest_seq


# Example:
# lst = [1, 2, 3, 1, 4, 5]
# Output: [2, 3, 1, 4, 5]
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# 2. ONLINE SHOPPING PRICE ANALYSIS
# Maximum sum of a continuous subarray
# Kadane's Algorithm

def OnlineShoppingPrice(lst):

    cur_sum = lst[0]
    max_sum = lst[0]

    start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(lst)):

        if lst[i] > cur_sum + lst[i]:
            cur_sum = lst[i]
            start = i
        else:
            cur_sum += lst[i]

        if cur_sum > max_sum:
            max_sum = cur_sum
            best_start = start
            best_end = i

    return max_sum, best_start, best_end


# Example:
# lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: (6, 3, 6)
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# 3. RAIN WATER COLLECTION
# Calculate total trapped rainwater

def RainWater(lst):

    n = len(lst)

    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = lst[0]

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], lst[i])

    right_max[n - 1] = lst[n - 1]

    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], lst[i])

    total_water = 0

    for i in range(n):

        water_level = min(left_max[i], right_max[i])

        water = water_level - lst[i]

        total_water += water

    return total_water


# Example:
# lst = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# 4. EMPLOYEE PERFORMANCE ANALYSIS
# Maximum sum continuous period
# Kadane's Algorithm

def EmployeePerformance(scores):

    cur_sum = scores[0]
    max_sum = scores[0]

    start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(scores)):

        if scores[i] > cur_sum + scores[i]:
            cur_sum = scores[i]
            start = i
        else:
            cur_sum += scores[i]

        if cur_sum > max_sum:
            max_sum = cur_sum
            best_start = start
            best_end = i

    return max_sum, best_start, best_end


# Example:
# scores = [-2, 3, -1, 5, -6, 4]
# Output: (7, 1, 3)
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# 5. PRODUCT SALES ANALYSIS
# Maximum product of a continuous subarray

def ProductAnalysis(sales_data):

    max_product = sales_data[0]
    min_product = sales_data[0]

    result = sales_data[0]

    for i in range(1, len(sales_data)):

        current = sales_data[i]

        # Negative number can turn minimum into maximum
        if current < 0:
            max_product, min_product = min_product, max_product

        max_product = max(current, max_product * current)
        min_product = min(current, min_product * current)

        result = max(result, max_product)

    return result


# Example:
# sales_data = [2, 3, -2, 4]
# Output: 6
#
# Your original code had:
# for i in len(n):
#
# It should be:
# for i in range(n)
#
# But prefix/suffix alone is not the best approach for this problem.
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# 6. CUSTOMER PURCHASE HISTORY
# Longest continuous sequence containing unique product IDs

def CustomerPurchaseHistory(lst):

    seen = set()

    left = 0
    longest_seq = []

    for right in range(len(lst)):

        while lst[right] in seen:
            seen.remove(lst[left])
            left += 1

        seen.add(lst[right])

        if right - left + 1 > len(longest_seq):
            longest_seq = lst[left:right + 1]

    return longest_seq


# Example:
# lst = [10, 20, 30, 20, 40, 50]
# Output: [30, 20, 40, 50]
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# 7. BANK TRANSACTION ANALYSIS
# Count continuous subarrays whose sum equals target

def BankTransactionAnalysis(lst, target):

    count = 0

    prefix_sum = 0

    seen = {0: 1}

    for num in lst:

        prefix_sum += num

        required = prefix_sum - target

        if required in seen:
            count += seen[required]

        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count


# Example:
# lst = [1, 2, 3, -2, 2]
# target = 3
# Output: 4
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# 8. EMPLOYEE SKILL GROUPING
# Group strings that contain the same characters
# Example: "eat", "tea", "ate" -> same group

def EmployeeSkillGrouping(lst):

    groups = {}

    for word in lst:

        key = ''.join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


# Example:
# lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# Output:
# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# 9. NETWORK PACKET ANALYSIS
# Longest consecutive numerical sequence
# Order in input does NOT matter

def longest_consecutive(packets):

    packets.sort()

    longest = 0
    count = 0
    previous = None

    for num in packets:

        if previous is None:
            count = 1

        elif num == previous:
            # Duplicate -> don't increase count
            pass

        elif num == previous + 1:
            count += 1

        else:
            count = 1

        longest = max(longest, count)

        previous = num

    return longest


# Example:
# packets = [100, 4, 200, 1, 3, 2]
# Output: 4
#
# Sequence = 1, 2, 3, 4
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
# 10. HOSPITAL APPOINTMENT SCHEDULING
# Merge overlapping intervals

def MergeAppointments(intervals):

    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:

        previous = merged[-1]

        if current[0] <= previous[1]:

            previous[1] = max(previous[1], current[1])

        else:

            merged.append(current)

    return merged


# Example:
# intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]
#
# Output:
# [[1, 6], [8, 12]]
#------------------------------------------------------------------------------#