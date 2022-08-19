import socket
import pickle
#serialise objects,s o mak eit bytes



class Network:
    def __init__(self):
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server="192.168.0.29"
        self.port=5555
        self.addr=(self.server,self.port)
        self.player=self.connect()
        #print(self.id)
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))#load byte data
        except:
            pass

    def send(self,data):
        try:
            self.client.send(pickle.dumps(data))#makes it bytes, encrypt,decompose
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    def get_player(self):
        return self.player
#n=Network()
#print(n.send("Working"))
#print(n.send("Working.."))
