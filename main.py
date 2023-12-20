import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('', 69)
sock.bind(server_address)

sock.listen(1)
print('ctrl+c to stop')

while True:
    connection, cl_address = sock.accept()
    try:
        print('Connect to: ', cl_address)
        while True:
            data = connection.recv(16)
            print(f'Пол.: {data.decode}')
            if data:
                data = data.upper()
                connection.sendall(data)
            else:
                print('Данные жок: ', cl_address)
                break
    finally:
        connection.close()