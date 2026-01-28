import os

if os.getenv('CI'):
  print('CI running...')
else:
  print('not CI running...')
