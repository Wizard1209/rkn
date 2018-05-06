'''Через дерево немного быстрее
Через заранее сгенерированный массив битов сильно быстрее
примерно половину времени занимает преобразование ip в двоичную запись
'''
from timeit import timeit

from rkn import RKN
from rkn1 import RKN1
from rkn2 import RKN2

stmt = '''
r.is_banned('87.251.23.31')
r.is_banned('87.252.23.31')
r.is_banned('87.250.255.255')
r.is_banned('8.231.4.4')
r.is_banned('9.2.8.7')
r.is_banned('192.168.0.0')
r.is_banned('192.168.0.1')
r.is_banned('255.168.1.1')
r.is_banned('255.168.0.1')
'''

r = RKN(['87.250.0.0/15', '8.8.8.8/8', '192.168.0.1/31'])
print(timeit(stmt=stmt, number=200000, globals={'r': locals().get('r')}))
# 22.5 секунды у меня

r = RKN1(['87.250.0.0/15', '8.8.8.8/8', '192.168.0.1/31'])
print(timeit(stmt=stmt, number=200000, globals={'r': locals().get('r')}))
# 20 секунд у меня

r = RKN2(['87.250.0.0/15', '8.8.8.8/8', '192.168.0.1/31'])
print(timeit(stmt=stmt, number=200000, globals={'r': locals().get('r')}))
# 6.5 секунд у меня
