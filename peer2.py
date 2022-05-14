from HashMap import HashMap
from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode

node_2 = MyOwnPeer2PeerNode("127.0.0.1", 8002, 2)

node_2.hash.add("h","Zummar")
node_2.hash.add("g","George")
node_2.hash.add("r","Folabi")

node_2.hash.print()

node_2.start()
