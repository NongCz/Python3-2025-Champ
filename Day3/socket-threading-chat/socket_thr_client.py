"""Client socket"""

import socket
import threading

HOST = '127.0.0.1' # server IP
PORT = 12345 # server port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to server")

    def send_message(client_socket):
        """
        Send message to server
        """
        while True:
            message = input("Enter message: ")
            client_socket.send((message+"\n").encode())

    while True:
        send_thread = threading.Thread(target=send_message, args=(s,))
        send_thread.start()

        message_received = ""
        while True:
            data = s.recv(1024)
            if data:
                # print('Received data chunk from server: ', repr(data))
                message_received += data.decode()

                if message_received.endswith("\n"):
                    break
            else:
                print("Connection lost!")
                break

        if message_received:
            print('Recieved message: ' + message_received)
        else:
            break

print("Client finished")