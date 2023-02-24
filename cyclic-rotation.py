def solution(A, K):
    # Implement your solution here
    len_A = len(A)

    sum = 0
    for i in range(len_A):
      sum = sum + A[i]
    if sum == 0:
      return(A)

    rotated_A = []
    for i in range(len_A):
      if i < (K % len_A):
        ele_rotated_A1 = A[i + len_A - (K % len_A)]
        rotated_A.append(ele_rotated_A1)
      if i >= (K % len_A):
        ele_rotated_A2 = A[i - (K % len_A)]
        rotated_A.append(ele_rotated_A2)
    return(rotated_A)
