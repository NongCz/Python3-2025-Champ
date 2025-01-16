import threading

def print_numbers():
    for i in range(10):
        print(i, end=' ')

def print_letters():
    for i in range(65, 75):
        print(chr(i), end=' ')

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print()
print('Thread done!')