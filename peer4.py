from HashMap import HashMap
from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode

node_4 = MyOwnPeer2PeerNode("127.0.0.1", 8004, 4)

node_4.hash.add("43","React")
node_4.hash.add("22","Java")


node_4.hash.print()

node_4.start()
