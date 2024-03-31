s = str(input("Enter sentence: "))

s_ = s.replace(' ', '')

key = int(input('Enter split key: '))

_l = list()

for i in range(len(s_)//key):
    _s = s_[i*key:(i+1)*key]
    _l.append(_s)

s_i = len(s_)
_li = len(_l)*key

if (s_i - _li != 0):
    last_ = s_[_li:s_i]
    _l.append(last_)

l_ = list()

for _i in _l:
    _il = list(_i)
    _il.reverse()
    
    l_.append(''.join(_il))


_l_ = list(''.join(l_))
_l_.reverse()
l = list()
space = 0

for i_ in range(len(s)):
    
    if (s[i_] == ' '):
        l.append(' ')
        space += 1
    else:    
        l.append(_l_[i_ - space])

print(''.join(l))