from bitarray import bitarray
import pregen as pg

class RKN2:
    def __init__(self, ip_list, pregenerated=False):
        if pregenerated:
            pregen = pg.hash_ipstofilename(ip_list)
            self.bits = bitarray()
            with open('data/' + pregen, 'rb+') as f:
                self.bits.fromfile(f)
        else:
            # generate bitarray for subnets list(ip_list)
            self.bits = pg.generate(ip_list)
        
    def is_banned(self, ip):
        num = pg.ip_to_num(ip)
        return self.bits[num]

    def clear(self):
        del(self.bits)

if __name__ == "__main__":
    r = RKN2(['10.0.0.0/8', '8.8.8.8/32', '192.168.0.1/24'], pregenerated=True)
    assert r.is_banned('10.1.2.3') == True
    assert r.is_banned('127.0.0.1') == False
    assert r.is_banned('8.8.8.8') == True
    assert r.is_banned('8.8.8.7') == False
    r.clear()
    r = RKN2(['87.250.0.0/15', '8.8.8.8/8', '192.168.0.1/31'], pregenerated=True)
    assert r.is_banned('87.251.23.31') == True
    assert r.is_banned('87.252.23.31') == False
    assert r.is_banned('87.250.255.255') == True
    assert r.is_banned('87.250.0.0') == True
    assert r.is_banned('87.251.255.255') == True
    assert r.is_banned('87.249.0.0') == False
    assert r.is_banned('87.252.0.0') == False
    assert r.is_banned('8.231.4.4') == True
    assert r.is_banned('9.2.8.7') == False
    assert r.is_banned('192.168.0.0') == True
    assert r.is_banned('192.168.0.1') == True
    assert r.is_banned('255.168.1.1') == False
    assert r.is_banned('255.168.0.1') == False
    r.clear()
