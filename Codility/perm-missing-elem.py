def solution(A):
    # Implement your solution here
    total = sum(A)
    len_A = len(A)
    full_total = (len_A + 2) * (len_A + 1) // 2
    missing_number = full_total - total
    return(missing_number)
