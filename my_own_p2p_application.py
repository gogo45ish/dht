import sys
import time
from peer1 import node_1
from peer2 import node_2
from peer3 import node_3
from peer4 import node_4
sys.path.insert(0, '..')  # Import the files where the modules are located

from MyOwnPeer2PeerNode import MyOwnPeer2PeerNode
from HashMap import HashMap

def select_node(node):
    match node:
        case "1":
            return node_1
        case "2":
            return node_2
        case "3":
            return node_3
        case "4":
            return node_4

if __name__ == '__main__':
    debug = False
    node_1.debug = debug
    node_2.debug = debug
    node_3.debug = debug
    node_4.debug = debug

    node_1.connect_with_node('127.0.0.1', 8002)
    node_2.connect_with_node('127.0.0.1', 8003)
    node_3.connect_with_node('127.0.0.1', 8004)
    node_4.connect_with_node('127.0.0.1', 8001)

    time.sleep(2)


    while 1:
        node = input("Select node: \n"
                     "# 1) Node 1\n"
                     "# 2) Node 2\n"
                     "# 3) Node 3\n"
                     "# 4) Node 4\n")
        node = select_node(node)
        command = input("Select Command: \n"
                        "# 1) List content \n"
                        "# 2) Get <Key> \n"
                        "# 3) Put <Key> <Value> \n"
                        "# 4) Delete <Key>\n")

        command = command.split()
        print(command[0])
        if command[0] == "get":
           node.get(command[1])
        elif command[0] == "put":
            node.add(command[1], command[2])
        elif command[0] == "delete":
            node.delete(command[1])
        elif command[0] == "list":
            node.hash.print()