import rpyc
from rpyc.utils.server import ThreadedServer

print("starter")

class MyService(rpyc.Service):
    # My service
    def exposed_pr(self, text):
        print(text)

if __name__ == "__main__":
    server = ThreadedServer(MyService, port = 18812)
    server.start()