import SocketServer

SERV_ADDR = ('localhost', 9999)
outFileName = './in_stream.asc'


class ReqHdl(SocketServer.StreamRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        if 'Tx' in data:
            with open(outFileName, 'w+') as outFile:
                while data:
                    self.request.send('OK')
                    outFile.write(data)
                    # spi_data.append(log2spi(data))
                    # self.request.send('OK')
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

    server.server_bind()
    server.server_activate()
    server.serve_forever()

if __name__ == '__main__':
    server_run(SERV_ADDR)