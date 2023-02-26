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

# Another solution
# source: https://codility-solutions.com/lessons/lesson-2-arrays/cyclicrotation/
def solution(A, K):
    # Implement your solution here
    temp = 0
    len_A = len(A)

    if len_A < 1:
        return A

    for i in range(K%len_A):
        temp = A[len_A-1]
        for j in range(len_A-1, 0, -1):
            A[j] = A[j-1]
        A[0] = temp
    return A
