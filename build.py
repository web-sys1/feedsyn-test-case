import subprocess

def entry_point():
   """ We use these conditions to check the statement"""
   subscriptions = [
     'http://feeds.feedburner.com/jblanton',
     'http://feeds.feedburner.com/IgnoreTheCode',
     'http://indiestack.com/feed/',
     'http://feedpress.me/inessential',
     'http://feeds.feedburner.com/JamesFallows',
     'http://feeds.feedburner.com/theendeavour',
     'http://feed.katiefloyd.me/',
     'http://feeds.feedburner.com/KevinDrum',
     'http://www.kungfugrippe.com/rss',
     'http://lancemannion.typepad.com/lance_mannion/rss.xml',
     ]
   with open(f'feeds.txt', 'w', encoding='utf8') as f:
     f.write(",".join(subscriptions).replace(',', '\n'))

"""Then initialize code."""
entry_point()
