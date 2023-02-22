#source: https://stackoverflow.com/a/60488617
def solution(A):
    max_A=max(A)
    B=set([a if a>=0 else 0 for a in A ])
    b=1
    if max_A<=0:
        return(1)
    else:
        while b in B:
            b+=1
        return(b)
