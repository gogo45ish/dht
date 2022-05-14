from p2pnetwork.node import Node
from HashMap import HashMap

class MyOwnPeer2PeerNode(Node):
    def __init__(self, host, port, id=None, callback=None, max_connections=0, hash=None):
        if hash is None:
            hash = HashMap();
        self.hash = hash
        super(MyOwnPeer2PeerNode, self).__init__(host, port, id, callback, max_connections)
        print("MyPeer2PeerNode: Started")

    # All the methods below are called when things happen in the network.
    # implement your network node behavior to create the required functionality.

    def outbound_node_connected(self, node):
        print("outbound_node_connected (" + self.id + "): " + node.id)

    def inbound_node_connected(self, node):
        print("inbound_node_connected: (" + self.id + "): " + node.id)

    def inbound_node_disconnected(self, node):
        print("inbound_node_disconnected: (" + self.id + "): " + node.id)

    def outbound_node_disconnected(self, node):
        print("outbound_node_disconnected: (" + self.id + "): " + node.id)

    def node_message(self, node, data):
        message = data.split()
        if message[0] == "find":
            self.get(message[1])
        else:
            print("node_message (" + self.id + ") from " + node.id + ": " + str(data))

    def node_disconnect_with_outbound_node(self, node):
        print("node wants to disconnect with oher outbound node: (" + self.id + "): " + node.id)

    def node_request_to_stop(self):
        print("node is requested to stop (" + self.id + "): ")

    # def send_to_node(self, n, data, compression='none'):
    #     print()

    def assign_successor(self,id):
        self.successor = id
    def find_successor(self):
        return self.successor

    def add(self, key,value):
        hash = self.hash
        hash.add(key,value)
    def delete(self, key):
        hash = self.hash
        hash.delete(key)
        print("Key "+key+"deleted")
    def get(self,key):
        hash = self.hash

        if hash.get(key) is None:
            self.send_to_node(self.nodes_outbound[0],"find "+key)
        else:
            print("node (" + self.id + ") I have this key! Which is")
            print(hash.get(key))

