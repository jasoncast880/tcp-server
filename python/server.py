# server.py:
# tcp server: connect to port 8081 and serve packets. 
# Start single-threaded, then graduate to a multithreaded , ie m-server.py

import socket

host = '0.0.0.0'
port = 8888 

# create a tcp/ip socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the address and port
server_socket.bind((host,port))

# listen for incoming connections
server_socket.listen(1)
print('Server Listening on all traffic')

while True:
    # accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    client_socket.close()

