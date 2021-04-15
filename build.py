import subprocess
from NFSyndication.extras import exist_template
from NFSyndication import styles

"""
def entry_point():
   """ We use these conditions to check the statement"""
   subscriptions = [
     'http://feeds.feedburner.com/jblanton',
     'http://feeds.feedburner.com/IgnoreTheCode',
     ]
   with open(f'feeds.txt', 'w', encoding='utf8') as f:
     f.write(",".join(subscriptions).replace(',', '\n'))
   return NFS_init.run()
"""

"""Then initialize code."""
exist_template()
