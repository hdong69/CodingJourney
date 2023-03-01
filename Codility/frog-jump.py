def solution(X, Y, D):
    # Implement your solution here
    distance = Y - X
    E = distance // D
    F = distance % D

    if F == 0:
        return E
    else:
        return (E+1)

