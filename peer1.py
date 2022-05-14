from HashMap import HashMap
from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode

node_1 = MyOwnPeer2PeerNode("127.0.0.1", 8001, 1)


node_1.hash.add("1","Ask")
node_1.hash.add("2","B")
node_1.hash.add("3","C")
node_1.hash.add("4","D")
node_1.hash.add("5","E")

node_1.hash.print()
node_1.start()
