# https://www.youtube.com/watch?v=rX5U32BPBXw&t=514s

def solution(l, t):
  sub_lists = list()
  if sum(l) < t:
    return [-1,-1]
  else:
    for start in range(len(l)):
      for end in range(1, len(l)):
        sub_list = l[start:end + 1]
        if sum(sub_list) == t:
          return sub_list
    return [-1,-1]
