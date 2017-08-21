from generate_sdes import *

ptext = '01110010'

def ep(key): return '{3}{0}{1}{2}{1}{2}{3}{0}'.format(*key)

def p4(key): return '{1}{3}{2}{0}'.format(*key)

def ip(key): return '{1}{5}{2}{0}{3}{7}{4}{6}'.format(*key)

def xor(key1, key2): return ''.join('0' if i == j else '1' for i, j in zip(key1,key2))

hold = ip(ptext)
left, right = split(hold)
hold2 = ep(right)
hold3 = xor(hold2, key2)
xor_out1, xor_out2 = split(hold3)

