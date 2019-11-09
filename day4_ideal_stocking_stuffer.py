import timeit, hashlib
start = timeit.default_timer()

print(hashlib.md5(b'abcdef609043').hexdigest())
byte = 'abcdef' + str(609043)
print('byte')
print(hashlib.md5(str(byte).encode()).hexdigest())

i = 0
found = False

while not found:

    byte = 'ckczppom' + str(i)
    if hashlib.md5(str(byte).encode()).hexdigest()[:6] == '000000':
        found = True
    if i % 10000 == 0:
        print(i)
    i += 1

print(i - 1)

stop = timeit.default_timer()
print('Time: ', stop - start)