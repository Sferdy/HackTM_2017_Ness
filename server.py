import SocketServer
import threading
import socket
import sys
from os.path import dirname, abspath, join
from config import SERVER_ADDR
from manip import log2spi

inFileName = join(dirname(abspath(__file__)), r'CANoe/HackTM2017_CANoe_Log/Logging.asc')
outFileName = join(dirname(abspath(__file__)), r'CANoe/HackTM2017_CANoe_Log/outFile.txt')

spi_data = []


# def find_host_with_mac_address(mac_addr):
#     nm = nmap.PortScanner()

class ReqHdl(SocketServer.StreamRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        if 'Tx' in data:
			while data:
				self.request.send('OK')
				sys.stdout.write(data)
				data = self.recv(1024)
           # with open(outFileName, 'w+') as outFile:
           #     while data:
           #         outFile.write(data)
           #         spi_data.append(log2spi(data))
           #         self.request.send('OK')
           #         data = self.request.recv(1024)

        # while data:
        #     print "Server received: ", data
        #     # echo data back
        #     data = data.upper()
        #     self.request.sendall(data)
        #     print "Server sent: ", data
        #     data = self.request.recv(1024)

def client_run(server_address):
    target = socket.socket()
    while target.connect_ex(server_address): pass
    with open(inFileName, 'r') as inFile:
        for line in inFile:
            target.sendall(line)
            print("Client sent: ", line)
            response = target.recv(1024)
            if response == 'OK': pass
            else: break


def server_run(server_address):
    server = SocketServer.ThreadingTCPServer(
        server_address=server_address
        , RequestHandlerClass=ReqHdl
        , bind_and_activate=False
    )
    # configure server
    server.daemon_threads = False
    server.allow_reuse_address = True
    server.request_queue_size = 1

    server.server_bind()
    server.server_activate()
    server.serve_forever()

if __name__ == '__main__':
#    server_thr = threading.Thread(target=server_run, args=(SERVER_ADDR,))
#    client_thr = threading.Thread(target=client_run, args=(SERVER_ADDR,))

#    server_thr.start()
#    client_thr.start()

	server_run()






