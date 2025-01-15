"""Client socket"""

import socket

HOST = '127.0.0.1' # server IP
PORT = 12345 # server port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

    while True:
        message = input("Enter a message('exit' to terminated): ")
        s.send((message+"\n").encode())

        if message == "exit":
            break

        message_received = ""
        while True:
            data = s.recv(1024)
            if data:
                print('Received data chunk from server: ', repr(data))
                message_received += data.decode()

                if message_received.endswith("\n"):
                    break
            else:
                print("Connection lost!")
                break

        if message_received:
            print(message_received)
        else:
            break

print("Client finished")