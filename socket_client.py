import socket

# #initiailze a socket client (ipv4 and tcp oriented connection)
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# def initialize_socket(host_ip,port):
#     s.connect((host_ip,port))
    

# def send_data(data):
#     s.send(data.encode())

# def recv_data():
#     data = s.recv(100).decode()
#     return data

# def close_connection():
#     s.close()


class Client_Socket:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def initialize_socket(self,host_ip,port):
        self.s.connect((host_ip,port))

    def send_data(self,data):
        self.s.send(data.encode())

    def close_connection(self):
        self.s.close()
