'''
rename a file or folder with timestamp
to avoid duplicate names
'''

import time, sys, os, datetime

if len(sys.argv) < 2:
	print 'feed me a file or folder'
	os.system('pause')
else:
	fname = sys.argv[1]
	words = fname.split('.')
	if os.path.exists(fname):
		ftime = os.stat(fname).st_mtime
		time_str = datetime.datetime.fromtimestamp(ftime).strftime('%b%d.%H%M')
		if time_str is not None:
			if len(words) == 1:
				words.append(time_str)
			else:
				words.insert(-1, time_str)
			new_fname = '.'.join(words)
			os.rename(fname, new_fname)