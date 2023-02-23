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
