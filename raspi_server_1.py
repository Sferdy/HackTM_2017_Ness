import SocketServer
from os.path import dirname, abspath, join

SERV_ADDR = ('10.1.0.16', 9999)
outFileName = join(dirname(abspath(__file__)), 'in_stream.asc')


class ReqHdl(SocketServer.StreamRequestHandler):

    def handle(self):
        with open(outFileName, 'w+') as outFile:
            data = self.request.recv(1024)
            while data:
                print(data)
                if 'Tx' in data:
                    outFile.write(data)
                data = self.request.recv(1024)

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
    try:
        server.server_bind()
        print("Server socket bound to address: ", SERV_ADDR)
        server.server_activate()
        print("Server socket listening...")
        server.serve_forever()
    finally:
        server.server_close()
        print("Server closed...")


if __name__ == '__main__':
    server_run(SERV_ADDR)
