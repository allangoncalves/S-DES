##### S-DES

def permute10(key): return '{2}{4}{1}{6}{3}{9}{0}{8}{7}{5}'.format(*key)

def permute8(key): return '{5}{2}{6}{3}{7}{4}{9}{8}'.format(*key)

def leftshift(key, perm): return key[perm:] + key[:perm]

def split(key): return [key[:len(key)//2], key[len(key)//2:]]


encryp = '1010000010'

p10 = permute10(encryp)
half1, half2 = split(p10)
shifted1 = leftshift(half1, 1)
shifted2 = leftshift(half2, 1) 
key1 = permute8(shifted1 + shifted2)
print('key1: %s' %(key1))
hold2 = leftshift(shifted1, 2) + leftshift(shifted2, 2)
key2 = permute8(hold2)
print('key2: %s' %(key2))


	
 




