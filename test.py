base_str = ''.join(random.choice(string.ascii_lowercase) for i in range(100000000))
start_time = time.time()
durations = []

dictionary = {}

for i in range(26):
    dictionary[string.ascii_lowercase[i]] = i

start_time = time.time()
result = []
for c in base_str:
    result.append(dictionary[c])
durations.append(time.time() - start_time)

start_time = time.time()
result = []
for c in base_str:
    result.append(ord(c)-97)
durations.append(time.time() - start_time)



print(durations)
