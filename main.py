import os
from datetime import datetime

print(datetime.now())

if os.getenv('CI'):
  print('CI running...')
else:
  print('not CI running...')

print('test webhook ...')
