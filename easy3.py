def generate_pascals_triangle(row_num):
    if row_num <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, row_num):
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])

        new_row.append(1)
        triangle.append(new_row)

    return triangle

# Example: Get the Pascal's Triangle row for row number 5
row_number = 5
result = generate_pascals_triangle(row_number)
print(result)
