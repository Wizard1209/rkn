from bitarray import bitarray
from hashlib import sha1

def generate(ips):
    res = bitarray(2**32)
    for i in ips:
        ip, bits = i.split('/')
        bits = int(bits)
        num_repr = ip_to_num(ip)
        mask = netmask(bits)
        # first ip in subnet
        start = num_repr & mask
        # last ip in subnet
        end = (num_repr & mask) + (2**(32-bits) - 1)
        res[start:end + 1] = True
    return res

def netmask(bits):
    return 2**32 - 2**(32-bits)

def ip_to_num(ip):
    tmp = ip.split('.')
    num = (int(tmp[0]) << 24) + (int(tmp[1]) << 16) + \
        (int(tmp[2]) << 8) + int(tmp[3])
    return num
    
def hash_ipstofilename(ips):
    m = sha1()
    for i in ips:
        m.update(i.encode())
    return m.hexdigest()

if __name__ == "__main__":
    # ips = ['10.0.0.0/8', '8.8.8.8/32']
    # ips = ['87.250.0.0/15', '8.8.8.8/8', '192.168.0.1/31']
    ips = ['10.0.0.0/8', '8.8.8.8/32', '192.168.0.1/24']
    res = generate(ips)
    file = hash_ipstofilename(ips)
    with open('data/'+file, 'wb+') as f:
        res.tofile(f)
    del(res)
