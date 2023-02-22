def solution(N):
    # Implement your solution here
    temp_binary = bin(N)
    right_binary = temp_binary.replace("0b", "")
    components_split=right_binary.split("1")
    max = 0
    if components_split[len(components_split)-1] != "":
      return 0
    for i in range(len(components_split)):
      if max < len(components_split[i]):
        max = len(components_split[i])
    return(max)
