import bs4
import requests
import time
from time import monotonic

a = {}
i = 0
while True:
    if input() == 'ку':
        i += 1
        start_time = time.time()
        player = f'player{i}'
        name = input()
        a.setdefault(player, [name, 10, start_time])
        print(a)

    t = monotonic()
    while True:
        if input() == 'ку':
            if round(time.time() - a[player][2]) < 5:
                print('wait')
            else:
                a[player][1] += 5
                start_time = time.time()
                a[player][2] = start_time
                print('+5', a[player][1])


