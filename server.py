import SocketServer
import threading
import socket
import sys
from os.path import dirname, abspath, join

SERVER_ADDR = 'localhost'
PORT = 9999
inFileName = ''

def stdin2file(file):
    sys.stdin = file

class ReqHdl(SocketServer.StreamRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        while data:
            print "Server received: ", data
            # echo data back
            data = data.upper()
            self.request.sendall(data)
            print "Server sent: ", data
            data = self.request.recv(1024)

def client_run(server_address):
    target = socket.socket()
    while target.connect_ex(server_address): pass
    data = sys.stdin.readline()
    while(data):
        target.sendall(data)
        print "Client sent: ", data
        data = target.recv(1024)
        print "Client received: ", data
        data = sys.stdin.readline()

def server_run(server_address):
    server = SocketServer.ThreadingTCPServer(
        server_address=server_address
        , RequestHandlerClass=ReqHdl
        , bind_and_activate=False
    )
    server.daemon_threads = False
    server.allow_reuse_address = True
    server.server_bind()
    server.server_activate()
    server.serve_forever()

if __name__ == '__main__':
    server_thr = threading.Thread(target=server_run, args=((SERVER_ADDR, PORT),))
    client_thr = threading.Thread(target=client_run, args=((SERVER_ADDR, PORT),))

    server_thr.start()
    client_thr.start()






