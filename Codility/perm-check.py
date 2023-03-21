# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    N = len(A)
    total = sum(A)
    total_format = N*(N+1)/2
    
    if len(set(A)) == N and total == total_format:
        return 1
    
    return 0

# another solution
# source: https://stackoverflow.com/a/56525918
def solution(A):

    le = len(A)
    A = list(set(A))

    if le != len(A):
        return 0

    le = len(A)

    if le != max(A):
        return 0

    return 1
