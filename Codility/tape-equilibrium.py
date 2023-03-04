def solution(A):
    # Implement your solution here
    len_A = len(A)
    total_A = sum(A)
    sum_1st_part = 0
    sum_last_part = 0
    diff_array = []

    for p in range(1, len_A):
        sum_1st_part = sum_1st_part + A[p-1]
        sum_last_part = total_A - sum_1st_part
        diff = abs(sum_1st_part - sum_last_part)
        diff_array.append(diff)

    x = min(diff_array)
    return(x)
