import time

start = time.time()
while time.time() - start < 21:
    remaining_time = 20 - int(time.time() - start)
    print(remaining_time)
    time.sleep(1)
