import time
epoch = time.time()
print(epoch)
#dt = time.localtime(seconds-since-epoch)

t = time.localtime()
# retrieve date
d = t.tm_mday
m = t.tm_mon
y = t.tm_year
print('Current date is : %d - %d -%d' %(d, m, y))
print()
# retrieve time
h = t.tm_hour
m = t.tm_min
s = t.tm_sec
print('Current time id : %d : %d : %d' %(h, m, s))
print()

# Another way using ctime
t = time.ctime()
print(t)
print()

