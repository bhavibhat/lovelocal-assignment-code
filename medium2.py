def majority_elements(nums):
    if not nums:
        return []

    candidate1, candidate2, count1, count2 = 0, 1, 0, 0

    # First pass: Find potential candidates
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Second pass: Confirm candidates
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    n = len(nums)

    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    return result

# Example usage
nums = [3,2,3]
result = majority_elements(nums)
print(result)
