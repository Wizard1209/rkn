class Node:
    def __init__(self):
        self.z = None # zero
        self.o = None # one
        self.issub = False # is subtree;leaf

class Tree:
    def __init__(self, ips):
        self.root = Node()
        for i in ips:
            self.add(i)
        
    def add(self, val):
        n = self.root
        for i in val:
            if i == '0':
                if n.z == None:
                    n.z = Node()
                n = n.z
            if i == '1':
                if n.o == None:
                    n.o = Node()
                n = n.o

        n.issub = True
                    
    def find(self, val):
        n = self.root
        for i in val:
            if i == '0':
                if n.issub == True:
                    return True
                if n.z == None:
                    return False
                n = n.z
            if i == '1':
                if n.issub == True:
                    return True
                if n.o == None:
                    return False
                n = n.o

        return n.issub
        
class RKN1:
    def __init__(self, ip_list):
        ips = []
        for i in ip_list:
            ip, bits = i.split('/')
            ips.append(RKN1.ip_to_bin(ip)[:int(bits)])
        self.tree = Tree(ips)
        
    def is_banned(self, ip):
        bi = RKN1.ip_to_bin(ip)
        return self.tree.find(bi)

    # функция преобразующая ip в двоичную запись
    @staticmethod
    def ip_to_bin(ip):
        return '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*map(int, ip.split('.')))


if __name__ == "__main__":
    r = RKN1(['10.0.0.0/8', '8.8.8.8/32', '192.168.0.1/24'])
    assert r.is_banned('10.1.2.3') == True
    assert r.is_banned('127.0.0.1') == False
    assert r.is_banned('8.8.8.8') == True
    assert r.is_banned('8.8.8.7') == False
    r = RKN1(['87.250.0.0/15', '8.8.8.8/8', '192.168.0.1/31'])
    assert r.is_banned('87.251.23.31') == True
    assert r.is_banned('87.252.23.31') == False
    assert r.is_banned('87.250.255.255') == True
    assert r.is_banned('8.231.4.4') == True
    assert r.is_banned('9.2.8.7') == False
    assert r.is_banned('192.168.0.0') == True
    assert r.is_banned('192.168.0.1') == True
    assert r.is_banned('255.168.1.1') == False
    assert r.is_banned('255.168.0.1') == False
