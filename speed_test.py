'''Через дерево быстрее
также я сделал тесты, с максимизацией константы при поиске в дереве'''
from time import clock

from rkn import RKN
from rkn1 import RKN1

r = RKN1(['87.250.0.0/15', '8.8.8.8/8', '192.168.0.1/31'])
clock()
for i in range(100000):
    r.is_banned('87.251.23.31')
    r.is_banned('87.252.23.31')
    r.is_banned('87.250.255.255')
    r.is_banned('8.231.4.4')
    r.is_banned('9.2.8.7')
    r.is_banned('192.168.0.0')
    r.is_banned('192.168.0.1')
    r.is_banned('255.168.1.1')
    r.is_banned('255.168.0.1')

print(clock()) # ~10 секунд у меня
r = RKN(['87.250.0.0/15', '8.8.8.8/8', '192.168.0.1/31'])
clock()
for i in range(100000):
    r.is_banned('87.251.23.31')
    r.is_banned('87.252.23.31')
    r.is_banned('87.250.255.255')
    r.is_banned('8.231.4.4')
    r.is_banned('9.2.8.7')
    r.is_banned('192.168.0.0')
    r.is_banned('192.168.0.1')
    r.is_banned('255.168.1.1')
    r.is_banned('255.168.0.1')
    
print(clock()) # ~20 секунд у меня
