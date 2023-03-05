class Sender:
    def __init__(self, send_queue):
        self.send_queue = send_queue
        self.start()


    def start(self):
        while True:
            reply, sock = self.send_queue.get()
            sock.send(reply)
