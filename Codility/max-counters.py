# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # Implement your solution here
    counters = [0,] * N
    array_1st = []
    array_2nd = []
    
    if len(A) == 1 and A[0] == 1 and N <= len(A):
        return [1]

    for i in range(0, A.index(max(A))):
        array_1st.append(A[i])

    for j in array_1st:
        counters[j-1] += 1

    for i in range(0, N):  
        counters[i] = max(counters)
  
    for i in range(A.index(max(A))+1, len(A)):
        array_2nd.append(A[i])

    for t in array_2nd:
        counters[t-1] += 1

    return(counters)
