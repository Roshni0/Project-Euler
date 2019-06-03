import time
start_time = time.time()

pandigs = []
digs = {str(i) for i in range(10)}
divs = [13, 11, 7, 5, 3, 2, 1]

for i in range(102, 983, 17):
    n = str(i)
    if (len(set(n)) == len(n)):
        pandigs.append(n)

for d in divs:
    temp = []
    for n in pandigs:
        av_digs = list(digs - set(n))
        for a in av_digs:
            t = a + n
            if (int(t[0:3])%d == 0):
                temp.append(str(t))
    pandigs = temp

pandigs = list(map(int, pandigs))

print(sum(pandigs))
