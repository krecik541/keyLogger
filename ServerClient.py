import socket
import threading


class ServerClient:
    HOST = '192.168.3.217'
    PORT = 8080
    message: str = ""
    s: socket = None


    def __init__(self):
        client_thread = threading.Thread(target=self.send)
        client_thread.daemon = True
        client_thread.start()
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.HOST, self.PORT))
        except:
            print("Error")

    def send(self):
        if self.message != "":
            self.s.sendall(str(f"{self.message} \n").encode())
            self.message = ""