def solution(steps, path):
  ud = {'U': 1, 'D': -1}
  position = 0
  valleys = 0
  for step in path:
    if position == 0 and step == 'D':
      valleys += 1
    position += ud[step]
  return valleys
