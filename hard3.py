def count_ones(n):
    count = 0
    multiplier = 1
    while multiplier <= n:
        divider = multiplier * 10
        count += (n // divider) * multiplier + min(max(n % divider - multiplier + 1, 0), multiplier)
        multiplier *= 10
    return count

# Example usage
n = 13
result = count_ones(n)
print(result)
