"""Server socket"""

import socket
import sys
# from pyexpat.errors import messages

HOST = '0.0.0.0' # accept connections from any IP
PORT = 12345 # port to listen on
s = None

# create socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
except OSError as msg:
    s = None
    print(f'Error creating socket: {msg}')
    sys.exit(1)

# bind and listen
try:
    s.bind((HOST, PORT))
    s.listen()
    print('Socket bound and listening')
except OSError as msg:
    print('Error binding/listening!')
    s.close()
    sys.exit(1)

conn, addr = s.accept()

with conn:
    print('Connection accepted from ', addr)
    while True:
        message_received = ''

        while True:
            data = conn.recv(1024)
            if data:
                if data.decode() == 'exit\n':
                    break
                print('Received data chunk from client: ', repr(data))
                message_received += data.decode()
                if message_received.endswith('\n'):
                    break
            else:
                print('Connection lost!')
                break

        if message_received:
            print('Received message: ', message_received)
            server_msg = input('Enter message to send to client: ')
            # conn.send(('Server summarized: ' + message_received[:10] + '\n').encode())
            conn.send(('Message from server: ' + server_msg + '\n').encode())
        else:
            break

s.close()
print('Server finished')