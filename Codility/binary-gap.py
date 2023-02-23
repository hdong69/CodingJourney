def solution(N):
    # Implement your solution here
    temp_binary = bin(N)
    right_binary = temp_binary.replace("0b", "")
    array = []
    for i in range(1, len(right_binary)+1):
      if right_binary.startswith('1', i-1):
        array.append(i)

    max = 0
    for i in range(1,len(array)):
      sub = array[i] - array[i-1]
      if max < sub - 1 :
        max = sub - 1
    return(max)

#Another solution
#source: https://stackoverflow.com/a/69917131
def solution(N):
    b=bin(N)[2:]
    return len(max(b.strip('0').split('1'))) 
# here strip will remove all trailing 0's and split will create a list with splitting 1's and combining 0's which are together.
