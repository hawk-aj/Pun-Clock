import time

t = time.localtime()
tt = time.strftime('%H:%M:%S',t)
print(t.tm_sec)