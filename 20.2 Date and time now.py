'''
ctime() - function of time module
now() - method of datetime class of datetime module
today() - method of datetime class of datetime module
'''

from datetime import *
now = datetime.now()
print(now)
print()
print('Date now : {}/{}/{}'.format(now.day, now.month, now.year))
print('Time now : {}:{}:{}'.format(now.hour, now.minute, now.second))
print()
