class RKN:
    def __init__(self, ip_list):
        self.subnets = set()
        for i in ip_list:
            ip, bits = i.split('/')
            self.subnets.add(RKN.ip_to_bin(ip)[:int(bits)])
        
    def is_banned(self, ip):
        bi = RKN.ip_to_bin(ip)
        for i in range(32, -1, -1):
            if bi[:i] in self.subnets:
                return True
        return False

    # функция преобразующая ip в двоичную запись
    @staticmethod
    def ip_to_bin(ip):
        return '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*map(int, ip.split('.')))


if __name__ == "__main__":
    r = RKN(['10.0.0.0/8', '8.8.8.8/32', '192.168.0.1/24'])
    assert r.is_banned('10.1.2.3') == True
    assert r.is_banned('127.0.0.1') == False
    assert r.is_banned('8.8.8.8') == True
    assert r.is_banned('8.8.8.7') == False
    r = RKN(['87.250.0.0/15', '8.8.8.8/8', '192.168.0.1/31'])
    assert r.is_banned('87.251.23.31') == True
    assert r.is_banned('87.252.23.31') == False
    assert r.is_banned('87.250.255.255') == True
    assert r.is_banned('8.231.4.4') == True
    assert r.is_banned('9.2.8.7') == False
    assert r.is_banned('192.168.0.0') == True
    assert r.is_banned('192.168.0.1') == True
    assert r.is_banned('255.168.1.1') == False
    assert r.is_banned('255.168.0.1') == False
