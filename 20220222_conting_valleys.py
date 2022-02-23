def countingValleys(steps, path):
  ud = {'U': 1, 'D': -1}
  position = 0
  valleys = 0
  for step in path:
    print('------')
    print(f'step: {ud[step]}')
    print(f'position: {position}')
    print(position == 0 and step == 'D')
    print('------')
    if position == 0 and step == 'D':
      # import ipdb; ipdb.set_trace(context=10)
      valleys += 1
    position += ud[step]
  return valleys

print(countingValleys(8, 'UDDDUDUU'))
