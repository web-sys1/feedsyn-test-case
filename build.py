from NFSyndication import __main__ as NFS_init

def entry_point():
    """ We use these conditions to check the statement"""
    subscriptions = [
     'https://www.tvmagia.ro/feed/',
     ]
  
    with open(f'feeds.txt', 'w', encoding='utf8') as f:
     f.write(",".join(subscriptions).replace(',', '\n'))
    return NFS_init.run()

"""Then initialize code."""
entry_point()
