#server side code
import socket
from datetime import datetime


server_socket =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="192.168.1.20"
port=8000

server_socket.bind((ip,port))
print("-----------------------")
print("SOCKET SERVER is listening at port 8000")
print("------------------------")
print("\n")
server_socket.listen(10)

while 1:

    #accept connection from client and receive the client socket object
    (client_socket,address) = server_socket.accept()
    print("Connection has been made with the monitoring system")
    #print("connection found!")
    while 1:
        data = client_socket.recv(100)
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("-------------")
        print(data.decode() + " detected in "+ date_time)
        print("-------------")
    #client_socket.send("Thank you for sending".encode())

    #close active session between the server and the client
    client_socket.close()