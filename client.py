import socket
import time
# from config import SERVER_ADDR, LOG_PATH

serv_addr = ('10.1.0.16', 9999)
log_path = './CANoe/Log/Logging.asc'

class Client:

    def __init__(self, server_addr):
        self.server_addr = server_addr
        try:
            self.run()
        finally:
            self.target.close()


    def run(self):
        self.target = socket.socket()
        while self.target.connect_ex(self.server_addr):
            print("[Client] Trying to connect to address: ", serv_addr)
            time.sleep(1)
        with open(log_path, 'r') as inFile:
            print("[Client] Connection to server achieved...")
            for line in inFile:
                print('[Client] Sent ', line)
                self.target.sendall(line)



if __name__ == '__main__':
    c = Client(serv_addr)