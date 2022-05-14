from HashMap import HashMap
from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode

node_3 = MyOwnPeer2PeerNode("127.0.0.1", 8003, 3)

node_3.hash.add("1231","Software")
node_3.hash.add("3442","Node")

node_3.hash.print()

node_3.start()
