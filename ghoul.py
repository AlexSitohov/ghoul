import time

for i in range(1000, 1, -7):
    time.sleep(0.1)
    if i != 1000:
        print(f'{i + 7} - {7} = {i}')