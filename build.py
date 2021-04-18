# build.py
import subprocess
from NFSyndication import init as NFS_init
from NFSyndication import styles

def entry_point():
   """ We use these conditions to check the statement"""
   subscriptions = [
     'http://blog.ashleynh.me/feed',
     'https://www.betalogue.com/feed/',
     'https://bitsplitting.org/feed/',
     ]
   with open(f'feeds.txt', 'w', encoding='utf8') as f:
     f.write(",".join(subscriptions).replace(',', '\n'))
   return NFS_init.run()

"""Then initialize code."""
entry_point()
